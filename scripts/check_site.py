#!/usr/bin/env python3
"""Check a built Jekyll site using only the Python standard library."""

import argparse
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit


CSS_COMMENTS = re.compile(r"/\*.*?\*/", re.S)
CSS_URLS = re.compile(r"url\(\s*(['\"]?)(.*?)\1\s*\)", re.I | re.S)
CSS_IMPORTS = re.compile(r"@import\s+(['\"])(.*?)\1", re.I)


class Document(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.assets = []
        self.anchors = set()
        self.fragments = []
        self.styles = []
        self.in_style = False
        self.feed(source)
        self.close()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.anchors.add(attrs["id"])
        if tag == "a" and attrs.get("name"):
            self.anchors.add(attrs["name"])
        for attribute in ("src", "poster"):
            if attrs.get(attribute):
                self.assets.append(attrs[attribute])
        if tag == "use" and attrs.get("href"):
            self.assets.append(attrs["href"])
        if tag == "link":
            rel = (attrs.get("rel") or "").lower().split()
            if any(item == "stylesheet" or "icon" in item for item in rel):
                if attrs.get("href"):
                    self.assets.append(attrs["href"])
        if tag == "a" and attrs.get("href"):
            href = attrs["href"]
            self.fragments.append(href)
            # Local downloads and video fallbacks are dependencies too.
            if Path(urlsplit(href).path).suffix.lower() in {
                ".pdf", ".mp4", ".webm", ".mov", ".zip", ".jpg", ".png", ".gif"
            }:
                self.assets.append(href)
        if attrs.get("style"):
            self.styles.append(attrs["style"])
        if tag == "style":
            self.in_style = True

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_endtag(self, tag):
        if tag == "style":
            self.in_style = False

    def handle_data(self, data):
        if self.in_style:
            self.styles.append(data)


def css_assets(source):
    source = CSS_COMMENTS.sub("", source)
    return [match[1].strip() for match in CSS_URLS.findall(source)] + [
        match[1].strip() for match in CSS_IMPORTS.findall(source)
    ]


def local_path(url, origin):
    """Resolve a browser-relative resource URL to a path within the site."""
    parsed = urlsplit(url.strip())
    if parsed.scheme or parsed.netloc or not parsed.path:
        return None
    return unquote(urlsplit(urljoin("/" + origin, url)).path).lstrip("/")


def check_site(root):
    errors = []
    dependencies = {}
    for source_dir in ("publications", "layouts"):
        if (root / source_dir).exists():
            errors.append(f"Source directory must not be published: {source_dir}/")
    for page in ("index.html", "GPS-Gaussian.html"):
        file = root / page
        if not file.is_file():
            errors.append(f"Missing page: {page}")
            continue
        document = Document(file.read_text(encoding="utf-8"))
        found = set()
        pending = [(url, page) for url in document.assets]
        for style in document.styles:
            pending.extend((url, page) for url in css_assets(style))
        while pending:
            url, origin = pending.pop()
            resource = local_path(url, origin)
            if resource is None or resource in found:
                continue
            found.add(resource)
            target = root / resource
            if not target.is_file():
                errors.append(f"Missing asset: {resource} (from {origin})")
                continue
            if target.suffix.lower() == ".css":
                pending.extend(
                    (url, resource)
                    for url in css_assets(target.read_text(encoding="utf-8"))
                )
        dependencies[page] = found
        if page == "index.html":
            for href in document.fragments:
                parsed = urlsplit(href)
                if parsed.scheme or parsed.netloc or not parsed.fragment:
                    continue
                if parsed.path and local_path(href, page) not in ("", "index.html"):
                    continue
                anchor = unquote(parsed.fragment)
                if anchor not in document.anchors:
                    errors.append(f"Missing homepage anchor: #{anchor}")
    for redirect in ("about/index.html", "about.html"):
        if not (root / redirect).is_file():
            errors.append(f"Missing redirect: {redirect}")
    return errors, dependencies


def compare_baseline(root, baseline, dependencies):
    errors = []
    for resource in sorted({"GPS-Gaussian.html"} | dependencies.get("GPS-Gaussian.html", set())):
        before, after = baseline / resource, root / resource
        if not before.is_file():
            errors.append(f"Baseline missing: {resource}")
        elif after.is_file() and before.read_bytes() != after.read_bytes():
            errors.append(f"GPS page or dependency changed: {resource}")
    before, after = baseline / "index.html", root / "index.html"
    if not before.is_file():
        errors.append("Baseline missing: index.html")
    elif after.is_file():
        expected = before.read_bytes().replace(b"/images/hfut.jpeg", b"/images/hfut.png")
        actual = after.read_bytes().replace(b"/images/hfut.jpeg", b"/images/hfut.png")
        if expected != actual:
            errors.append("Homepage HTML changed beyond the allowed hfut image path rename")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default="_site", type=Path, help="Jekyll output directory (default: _site)")
    parser.add_argument("--baseline", type=Path, help="Compare homepage HTML and GPS page/assets against an earlier build")
    args = parser.parse_args()
    errors, dependencies = check_site(args.root)
    if args.baseline:
        errors.extend(compare_baseline(args.root, args.baseline, dependencies))
    if errors:
        for error in dict.fromkeys(errors):
            print(f"ERROR: {error}")
        return 1
    count = len(set().union(*dependencies.values()))
    print(f"PASS: 2 pages, 2 redirects, homepage anchors, and {count} local assets checked in {args.root}")
    if args.baseline:
        print("PASS: homepage HTML and GPS page/dependencies match the baseline")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
