import pytest
import sys
from pathlib import Path
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from check_urls import check_url, check_all_urls


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
