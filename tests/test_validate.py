import json
import pytest
from pathlib import Path
import sys

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from validate import validate_schema, validate_version_format, validate_date_format


def test_validate_schema_valid():
    """Test that valid schema passes validation"""
    data = {
        "schema_version": "4.0.0",
        "packages": []
    }
    result = validate_schema(data)
    assert result is True


def test_validate_schema_missing_version():
    """Test that missing schema_version fails"""
    data = {"packages": []}
    result = validate_schema(data)
    assert result is False


def test_validate_version_format_valid():
    """Test valid semantic version"""
    assert validate_version_format("1.0.0") is True
    assert validate_version_format("10.20.30") is True


def test_validate_version_format_invalid():
    """Test invalid version formats"""
    assert validate_version_format("v1.0.0") is False
    assert validate_version_format("1.0") is False


def test_validate_date_format_valid():
    """Test valid date format"""
    assert validate_date_format("2025-01-12 00:00:00") is True


def test_validate_date_format_invalid():
    """Test invalid date formats"""
    assert validate_date_format("2025-01-12") is False
    assert validate_date_format("01/12/2025 00:00:00") is False
