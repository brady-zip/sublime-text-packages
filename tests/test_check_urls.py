import pytest
import sys
from pathlib import Path
from unittest.mock import Mock, patch
import importlib.util

# Load the check-urls module (hyphenated filename)
spec = importlib.util.spec_from_file_location(
    "check_urls",
    Path(__file__).parent.parent / "scripts" / "check-urls.py"
)
check_urls = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check_urls)

# Import the functions we need
check_url = check_urls.check_url
check_all_urls = check_urls.check_all_urls


def test_check_url_success():
    """Test successful URL check"""
    with patch('requests.head') as mock_head:
        mock_head.return_value.status_code = 200
        result = check_url("https://example.com")
        assert result is True


def test_check_url_not_found():
    """Test 404 URL check"""
    with patch('requests.head') as mock_head:
        mock_head.return_value.status_code = 404
        result = check_url("https://example.com/notfound")
        assert result is False


def test_check_all_urls_empty():
    """Test checking URLs with no packages"""
    data = {"schema_version": "4.0.0", "packages": []}
    result = check_all_urls(data)
    assert result is True
