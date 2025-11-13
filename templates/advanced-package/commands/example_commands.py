"""Example commands for PackageName"""
import sublime
import sublime_plugin
from ..lib import utils


class ExampleCommand1(sublime_plugin.TextCommand):
    """First example command"""

    def run(self, edit):
        settings = utils.get_settings()
        # Command implementation
        sublime.status_message("ExampleCommand1 executed!")


class ExampleCommand2(sublime_plugin.WindowCommand):
    """Second example command"""

    def run(self):
        # Command implementation
        sublime.status_message("ExampleCommand2 executed!")
