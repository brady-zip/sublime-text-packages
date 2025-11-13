# Testing Guide

How to test packages and validate the channel before publishing.

## Testing the Channel Locally

### Validate JSON

Check that `repositories.json` is valid:

```bash
python3 -m json.tool repositories.json
python3 scripts/validate.py
```

### Check URLs

Verify all package URLs are accessible:

```bash
python3 scripts/check-urls.py
```

### Test in Sublime Text

1. Start a local HTTP server:

```bash
cd ~/projects/sublime-text-packages
python3 -m http.server 8000
```

2. In Sublime Text, add the local channel:
   - Command Palette → "Package Control: Add Repository"
   - Enter: `http://localhost:8000/repositories.json`

3. Try installing a package:
   - Command Palette → "Package Control: Install Package"
   - Your packages should appear in the list

4. Clean up when done:
   - Command Palette → "Package Control: Remove Repository"
   - Remove `http://localhost:8000/repositories.json`

## Testing Packages in Development

### Method 1: Symlink to Packages Directory

```bash
# Find your Sublime Text packages directory:
# - macOS: ~/Library/Application Support/Sublime Text/Packages/
# - Linux: ~/.config/sublime-text/Packages/
# - Windows: %APPDATA%/Sublime Text/Packages/

# Create symlink
cd ~/Library/Application\ Support/Sublime\ Text/Packages/
ln -s ~/projects/my-package MyPackage
```

Restart Sublime Text. Your package is now loaded.

### Method 2: Copy to Packages Directory

```bash
cp -r ~/projects/my-package ~/Library/Application\ Support/Sublime\ Text/Packages/MyPackage
```

Restart Sublime Text after changes.

## Pre-Release Checklist

Before adding a package to the channel:

- [ ] Package has `package.json` with all required fields
- [ ] Package has README with installation and usage instructions
- [ ] Package has LICENSE file
- [ ] Package code follows Python best practices
- [ ] Package has been tested in Sublime Text
- [ ] GitHub repository has a tagged release
- [ ] Release archive URL is accessible
- [ ] `repositories.json` validates successfully
- [ ] URLs check passes

## Debugging

### Package Not Loading

1. Check the Sublime Text console (View → Show Console)
2. Look for Python errors related to your package
3. Common issues:
   - Syntax errors in Python code
   - Missing `__init__.py` in subdirectories
   - Incorrect imports

### Package Control Not Finding Package

1. Verify the channel URL is added correctly
2. Check Package Control console output:
   - Command Palette → "Package Control: List Packages"
   - Check console for error messages
3. Verify `repositories.json` is accessible via the URL
4. Validate JSON syntax and schema

### Commands Not Appearing

1. Check command names in Python match what's expected
2. Verify command is enabled (check `is_enabled()` method)
3. Look for errors in console
