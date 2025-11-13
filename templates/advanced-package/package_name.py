"""
PackageName - Main plugin entry point

Author: brady-zip
License: MIT
"""
import sublime
import sublime_plugin
from .lib import utils
from .commands import example_commands


def plugin_loaded():
    """Called when plugin is loaded"""
    print("PackageName: Plugin loaded")


def plugin_unloaded():
    """Called when plugin is unloaded"""
    print("PackageName: Plugin unloaded")
