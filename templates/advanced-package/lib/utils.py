"""Utility functions for PackageName"""
import sublime


def get_settings():
    """Get package settings"""
    return sublime.load_settings("PackageName.sublime-settings")


def get_setting(key, default=None):
    """Get a specific setting value"""
    return get_settings().get(key, default)
