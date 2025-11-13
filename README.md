# Sublime Text Packages

Public package channel for custom Sublime Text packages by brady-zip.

## Using This Channel

Add this repository to your Package Control:

1. Open Sublime Text
2. Open Command Palette (Cmd+Shift+P / Ctrl+Shift+P)
3. Select "Package Control: Add Repository"
4. Enter: `https://brady-zip.github.io/sublime-text-packages/repositories.json`

Now you can install packages from this channel via Package Control.

## Available Packages

Currently no packages are available. Check back soon!

## For Package Developers

- [Adding Packages](docs/adding-packages.md) - How to add packages to this channel
- [Package Structure](docs/package-structure.md) - Guide to creating Sublime Text packages
- [Testing](docs/testing.md) - How to test packages and the channel

## Repository Structure

```
sublime-text-packages/
├── repositories.json          # Package channel file
├── scripts/                   # Helper scripts
│   ├── validate.py           # Validate channel file
│   ├── check-urls.py         # Check package URLs
│   └── add-package.py        # Add packages to channel
├── templates/                 # Package templates
│   ├── basic-package/        # Simple package template
│   └── advanced-package/     # Full-featured template
└── docs/                      # Documentation
```

## License

MIT License - see LICENSE file for details
