# Sublime Text Package Structure

Guide to creating packages compatible with this channel.

## Basic Package Structure

For simple plugins with one or two commands:

```
package-name/
├── package.json              # Package metadata
├── README.md                 # Documentation
├── LICENSE                   # License file
├── .gitignore               # Git ignore rules
├── package_name.py          # Main plugin file
└── .github/
    └── workflows/
        └── release.yml      # Auto-release workflow
```

Use the basic template:

```bash
cp -r ~/projects/sublime-text-packages/templates/basic-package my-new-package
```

## Advanced Package Structure

For complex packages with multiple features:

```
package-name/
├── package.json
├── README.md
├── LICENSE
├── .gitignore
├── package_name.py          # Main entry point
├── PackageName.sublime-settings
├── lib/                     # Utility modules
│   ├── __init__.py
│   └── utils.py
├── commands/                # Command modules
│   ├── __init__.py
│   └── example_commands.py
└── .github/
    └── workflows/
        └── release.yml
```

Use the advanced template:

```bash
cp -r ~/projects/sublime-text-packages/templates/advanced-package my-new-package
```

## Package Metadata (package.json)

Required for Package Control:

```json
{
  "name": "PackageName",
  "description": "What your package does",
  "author": "brady-zip",
  "homepage": "https://github.com/brady-zip/package-name",
  "version": "1.0.0",
  "license": "MIT",
  "sublime_text": ">=3000"
}
```

## Python Code Guidelines

### Command Classes

Commands inherit from Sublime's base classes:

```python
import sublime
import sublime_plugin

# Text commands (operate on text in view)
class MyTextCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # edit parameter allows text modification
        pass

# Window commands (operate on windows)
class MyWindowCommand(sublime_plugin.WindowCommand):
    def run(self):
        # no edit parameter
        pass

# Application commands (global)
class MyApplicationCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        pass
```

### Plugin Lifecycle

```python
def plugin_loaded():
    """Called when plugin loads"""
    print("Plugin loaded")

def plugin_unloaded():
    """Called when plugin unloads"""
    print("Plugin unloaded")
```

### Settings

```python
import sublime

def get_settings():
    return sublime.load_settings("PackageName.sublime-settings")

def get_setting(key, default=None):
    return get_settings().get(key, default)
```

## Releasing

1. Update version in `package.json`
2. Commit changes
3. Create and push a tag:

```bash
git tag 1.0.0
git push origin 1.0.0
```

The GitHub Actions workflow will automatically create a release.

4. Add the release to the channel using `add-package.py`

## Resources

- [Sublime Text API Documentation](https://www.sublimetext.com/docs/api_reference.html)
- [Package Control Documentation](https://packagecontrol.io/docs)
