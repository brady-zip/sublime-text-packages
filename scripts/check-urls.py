#!/usr/bin/env python3
"""
Check that all package URLs in repositories.json are accessible.
"""
import json
import sys
from pathlib import Path
import requests


def check_url(url, timeout=10):
    """Check if URL is accessible"""
    try:
        response = requests.head(url, timeout=timeout, allow_redirects=True)
        return response.status_code == 200
    except requests.RequestException:
        return False


def check_all_urls(data):
    """Check all URLs in repositories data"""
    all_valid = True

    for pkg in data.get("packages", []):
        pkg_name = pkg.get("name", "unknown")

        # Check details URL
        details_url = pkg.get("details")
        if details_url:
            print(f"Checking {pkg_name} details URL...", end=" ")
            if check_url(details_url):
                print("✓")
            else:
                print(f"✗ Failed: {details_url}")
                all_valid = False

        # Check release URLs
        for release in pkg.get("releases", []):
            version = release.get("version", "unknown")
            url = release.get("url")
            if url:
                print(f"Checking {pkg_name} v{version} URL...", end=" ")
                if check_url(url):
                    print("✓")
                else:
                    print(f"✗ Failed: {url}")
                    all_valid = False

    return all_valid


def main():
    """Main URL checking function"""
    repo_file = Path(__file__).parent.parent / "repositories.json"

    if not repo_file.exists():
        print(f"Error: {repo_file} not found")
        return 1

    try:
        with open(repo_file) as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON - {e}")
        return 1

    if check_all_urls(data):
        print("\n✓ All URLs are accessible")
        return 0
    else:
        print("\n✗ Some URLs are not accessible")
        return 1


if __name__ == "__main__":
    sys.exit(main())
