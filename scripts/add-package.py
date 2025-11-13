#!/usr/bin/env python3
"""
Interactive script to add packages to repositories.json
"""
import json
import sys
from pathlib import Path
from datetime import datetime
import click


@click.command()
@click.option('--name', prompt='Package name', help='Name of the package')
@click.option('--details', prompt='Repository URL', help='GitHub repository URL')
@click.option('--version', prompt='Version', default='1.0.0', help='Release version')
@click.option('--url', prompt='Release URL', help='Download URL for the release')
@click.option('--date', default=None, help='Release date (YYYY-MM-DD HH:MM:SS, defaults to now)')
@click.option('--sublime-text', default='>=3000', help='Sublime Text version requirement')
def add_package(name, details, version, url, date, sublime_text):
    """Add a new package to repositories.json"""

    # Use current datetime if not provided
    if date is None:
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    repo_file = Path(__file__).parent.parent / "repositories.json"

    # Load existing data
    try:
        with open(repo_file) as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {"schema_version": "4.0.0", "packages": []}

    # Check if package already exists
    existing_pkg = None
    for pkg in data["packages"]:
        if pkg["name"] == name:
            existing_pkg = pkg
            break

    # Create release entry
    release = {
        "version": version,
        "url": url,
        "date": date,
        "sublime_text": sublime_text
    }

    if existing_pkg:
        # Add to existing package
        existing_pkg["releases"].append(release)
        click.echo(f"✓ Added version {version} to existing package '{name}'")
    else:
        # Create new package
        new_pkg = {
            "name": name,
            "details": details,
            "releases": [release]
        }
        data["packages"].append(new_pkg)
        click.echo(f"✓ Added new package '{name}' with version {version}")

    # Save updated data
    with open(repo_file, 'w') as f:
        json.dump(data, f, indent=2)
        f.write('\n')  # Add trailing newline

    click.echo(f"✓ Updated {repo_file}")


if __name__ == "__main__":
    add_package()
