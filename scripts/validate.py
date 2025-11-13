#!/usr/bin/env python3
"""
Validate repositories.json format and schema.
"""
import json
import sys
import re
from pathlib import Path
from jsonschema import validate as jsonschema_validate, ValidationError


SCHEMA = {
    "type": "object",
    "required": ["schema_version", "packages"],
    "properties": {
        "schema_version": {"type": "string"},
        "packages": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["name", "details", "releases"],
                "properties": {
                    "name": {"type": "string"},
                    "details": {"type": "string"},
                    "releases": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "required": ["version", "url", "date"],
                            "properties": {
                                "version": {"type": "string"},
                                "url": {"type": "string"},
                                "date": {"type": "string"},
                                "sublime_text": {"type": "string"}
                            }
                        }
                    }
                }
            }
        }
    }
}


def validate_schema(data):
    """Validate data against schema"""
    try:
        jsonschema_validate(instance=data, schema=SCHEMA)
        return True
    except ValidationError:
        return False


def validate_version_format(version):
    """Validate semantic version format (1.0.0)"""
    pattern = r'^\d+\.\d+\.\d+$'
    return bool(re.match(pattern, version))


def validate_date_format(date_str):
    """Validate date format (YYYY-MM-DD HH:MM:SS)"""
    pattern = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$'
    return bool(re.match(pattern, date_str))


def main():
    """Main validation function"""
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

    # Validate schema
    if not validate_schema(data):
        print("Error: Schema validation failed")
        return 1

    # Validate each package
    for pkg in data.get("packages", []):
        for release in pkg.get("releases", []):
            # Check version format
            version = release.get("version", "")
            if not validate_version_format(version):
                print(f"Error: Invalid version format '{version}' in package '{pkg['name']}'")
                return 1

            # Check date format
            date = release.get("date", "")
            if not validate_date_format(date):
                print(f"Error: Invalid date format '{date}' in package '{pkg['name']}'")
                return 1

    print("✓ Validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
