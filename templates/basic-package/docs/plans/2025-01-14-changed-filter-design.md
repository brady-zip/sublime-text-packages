# Changed Filter - Design Document

**Date:** 2025-01-14
**Package Name:** Changed Filter
**Author:** brady-zip

## Overview

Changed Filter is a Sublime Text package that provides quick navigation to git changed files with staging status filtering. Inspired by sublime-tabfilter and the LSP: Goto Symbol interface, it uses a hierarchical quick panel to filter and open files based on their git status.

## User Requirements

- Filter files by git status: All Changes, Staged Only, Unstaged Only
- Hierarchical drill-down interface (select filter → see filtered files)
- Compare working directory (staged + unstaged) against current HEAD commit
- Display full paths relative to git repository root
- Open selected file in a new tab
- Handle edge cases gracefully (not in git repo, no changed files)

## Architecture and Git Integration

### Core Architecture

The package consists of a single Python file (`changed_filter.py`) with three main components:

1. **ChangedFilterCommand** - A `WindowCommand` that launches the quick panel
2. **Git integration layer** - Functions to query git status and categorize files
3. **Quick panel handler** - Manages the hierarchical interface and user interaction

### Git Integration

We use Python's `subprocess` module to run git commands:

- `git rev-parse --git-dir` - Check if in a git repository
- `git rev-parse --show-toplevel` - Get git repository root path
- `git status --porcelain` - Get changed files with staging info

The porcelain format provides clean, parseable output:

```
M  staged_file.py          (staged modification)
 M unstaged_file.py        (unstaged modification)
MM both_staged_unstaged.py (staged + unstaged changes)
A  new_file.py             (staged new file)
?? untracked.py            (untracked file)
```

Files are categorized into:

- **Staged**: First character is not a space (M, A, D, R, etc.)
- **Unstaged**: Second character is not a space (M, D, etc.) or untracked (??)
- **All**: Union of both sets

Git commands execute from the project root to ensure consistent paths regardless of which file is currently open.

## Hierarchical Quick Panel Interface

### Two-Level Drill-Down

**Level 1 - Filter Selection:**

```
Changed Filter |

  All Changes (12 files)
  Staged Only (5 files)
  Unstaged Only (7 files)
```

**Level 2 - File List (after selecting "Staged Only"):**

```
Changed Filter | Staged Only |

  src/commands/filter.py
  src/utils/git.py
  README.md
  package.json
  tests/test_filter.py
```

### Navigation Flow

1. User opens "Changed Filter" command → sees filter options with file counts
2. User selects a filter → sees filtered file list
3. User selects a file → opens it in a new tab
4. User presses ESC from file list → returns to filter selection
5. User presses ESC from filter selection → closes panel

### Implementation Details

The quick panel uses `window.show_quick_panel()` with `on_done` callback to handle selection and navigate between levels.

## Data Structures and State Management

### State Variables

```python
self.git_root = None           # Path to git repository root
self.all_files = []            # All changed files: [(path, status), ...]
self.staged_files = []         # Filtered list of staged file paths
self.unstaged_files = []       # Filtered list of unstaged file paths
self.current_level = 'filter'  # 'filter' or 'files'
self.selected_filter = None    # 'all', 'staged', or 'unstaged'
```

### File Status Representation

Each file is stored as a tuple: `(file_path, status_code)` where status_code is the two-character git status:

- `'M '` - staged modification
- `' M'` - unstaged modification
- `'MM'` - both staged and unstaged
- `'A '` - staged new file
- `'??'` - untracked file

### Categorization Logic

```python
staged = first_char not in (' ', '?')
unstaged = second_char not in (' ') or status == '??'
```

This handles the edge case where a file can be both staged AND unstaged (staged a change, then made more changes).

### Error States

- **Not in git repo**: Show empty list with message "Not in a git repository"
- **No changed files**: Show empty list with message "No changed files"
- **Git command fails**: Show empty list with message "Error running git: {error}"

## Command Registration and User Experience

### Command Registration

Single command registered in the Command Palette:

- **Caption**: "Changed Filter" (user-facing)
- **Command ID**: `changed_filter` (internal)

**Default.sublime-commands:**
```json
[
    {
        "caption": "Changed Filter",
        "command": "changed_filter"
    }
]
```

### Optional Keyboard Shortcut

Suggested keybinding in `Default.sublime-keymap`:

```json
[
    {
        "keys": ["super+shift+g"],
        "command": "changed_filter"
    }
]
```

Users can customize or disable as preferred.

### Performance Considerations

- Git commands run synchronously (simple, and git status is fast - typically <100ms)
- Files sorted alphabetically for consistent ordering
- Paths relative to git root (cleaner display)

### Command Availability

The command is always available in Command Palette, even when not in a git repository. This allows users to see helpful error messages rather than wondering why the command is unavailable.

### Package Metadata

- **Package name**: Changed Filter
- **Description**: Quick panel filter for git changed files with staging status
- **Repository**: github.com/brady-zip/sublime-changed-filter
- **License**: MIT
- **Sublime Text Version**: >=3000

## Implementation Files

```
sublime-changed-filter/
├── changed_filter.py           # Main plugin file
├── Default.sublime-commands    # Command Palette registration
├── Default.sublime-keymap      # Optional keyboard shortcuts
├── package.json                # Package Control metadata
├── README.md                   # Documentation
├── LICENSE                     # MIT license
└── .github/
    └── workflows/
        └── release.yml         # Auto-release workflow
```

## Testing Strategy

1. Test in isolated environment (`/tmp/sublime-package-test-*`)
2. Test scenarios:
   - Repository with staged files only
   - Repository with unstaged files only
   - Repository with both staged and unstaged files
   - Repository with no changes
   - Not in a git repository
   - File with both staged and unstaged changes
3. Verify navigation flow (filter → files → open)
4. Verify ESC navigation (back to filter selection)

## Future Enhancements (Out of Scope for v1.0)

- Show git diff preview in panel
- Support for stash files
- Support for merge conflicts
- Configurable file sorting (by path, by type, by status)
- Icons for file status (added, modified, deleted)
