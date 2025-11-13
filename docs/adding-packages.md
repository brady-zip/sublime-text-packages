# Adding Packages to the Channel

This guide explains how to add packages to the brady-zip Sublime Text package channel.

## Prerequisites

- Package repository on GitHub (e.g., `github.com/brady-zip/my-package`)
- Tagged release in the package repository
- Python 3.8+ installed locally

## Method 1: Using add-package.py (Recommended)

The interactive script handles all the formatting:

```bash
cd ~/projects/sublime-text-packages
python3 scripts/add-package.py
```

You'll be prompted for:
- Package name
- Repository URL
- Version number
- Release download URL
- Release date (optional, defaults to now)
- Sublime Text version requirement (optional, defaults to >=3000)

The script will:
- Add the package to `repositories.json`
- Format everything correctly
- Update existing packages with new releases

## Method 2: Manual Addition

Edit `repositories.json` and add your package:

```json
{
  "schema_version": "4.0.0",
  "packages": [
    {
      "name": "YourPackageName",
      "details": "https://github.com/brady-zip/your-package",
      "releases": [
        {
          "version": "1.0.0",
          "url": "https://github.com/brady-zip/your-package/archive/refs/tags/1.0.0.zip",
          "date": "2025-01-12 00:00:00",
          "sublime_text": ">=3000"
        }
      ]
    }
  ]
}
```

### Important Notes

- **Version format:** Use semantic versioning without 'v' prefix (e.g., `1.0.0`, not `v1.0.0`)
- **Date format:** Must be `YYYY-MM-DD HH:MM:SS`
- **URL format:** Should point to GitHub release archive or tag archive
- **Sublime Text version:** Use format `>=3000` for ST3+, `>=4000` for ST4+

## Validation

Before committing, validate your changes:

```bash
# Check JSON syntax and schema
python3 scripts/validate.py

# Check that all URLs are accessible
python3 scripts/check-urls.py
```

## Publishing

Once validated, commit and push:

```bash
git add repositories.json
git commit -m "feat: add YourPackageName v1.0.0"
git push origin main
```

GitHub Actions will automatically validate your changes. If validation passes, the update will be live within a few minutes via GitHub Pages.

## Adding New Versions

To add a new version to an existing package:

1. Create a new release/tag in your package repository
2. Run `python3 scripts/add-package.py` with the same package name
3. The script will add the new release to the existing package entry

Or manually add a new entry to the `releases` array in `repositories.json`.
