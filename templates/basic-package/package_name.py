"""
PackageName - Brief description

Author: brady-zip
License: MIT
"""
import sublime
import sublime_plugin


class ExampleCommand(sublime_plugin.TextCommand):
    """Example command that can be called from Command Palette"""

    def run(self, edit):
        # Get current selection or entire file
        region = self.view.sel()[0] if self.view.sel() else sublime.Region(0, self.view.size())
        text = self.view.substr(region)

        # Do something with the text
        modified_text = text.upper()

        # Replace the text
        self.view.replace(edit, region, modified_text)

        # Show status message
        sublime.status_message("ExampleCommand executed!")

    def is_enabled(self):
        """Command is enabled when there's an active view"""
        return self.view is not None
