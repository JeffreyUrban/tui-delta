# TUI Delta

## ⚠️ Early Development - Not Ready for Use

**This project is under active development and is not ready for production use.**

- APIs may change without notice
- Documentation is incomplete
- No releases published yet
- Not accepting contributions at this time

> - **Star/watch the repo to be notified when the first release is available.**

**Run a TUI (terminal user interface) application with real-time delta processing**

[![PyPI version](https://img.shields.io/pypi/v/tui-delta.svg)](https://pypi.org/project/tui-delta/)
[![Tests](https://github.com/JeffreyUrban/tui-delta/actions/workflows/test.yml/badge.svg)](https://github.com/JeffreyUrban/tui-delta/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/JeffreyUrban/tui-delta/branch/main/graph/badge.svg)](https://codecov.io/gh/JeffreyUrban/tui-delta)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Documentation](https://img.shields.io/readthedocs/tui-delta)](https://tui-delta.readthedocs.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Installation

### Via Homebrew (macOS/Linux)

```bash
brew tap JeffreyUrban/tui-delta && brew install tui-delta
```

Homebrew manages the Python dependency and provides easy updates via `brew upgrade`.

### Via pipx (Cross-platform)

```bash
pipx install tui-delta
```

[pipx](https://pipx.pypa.io/) installs in an isolated environment with global CLI access. Works on macOS, Linux, and Windows. Update with `pipx upgrade tui-delta`.

### Via pip

```bash
pip install tui-delta
```

Use `pip` if you want to use tui-delta as a library in your Python projects.

### From Source

```bash
# Development installation
git clone https://github.com/JeffreyUrban/tui-delta
cd tui-delta-workspace/tui-delta
pip install -e ".[dev]"
```

**Requirements:** Python 3.9+

**IDE Configuration:**
- **PyCharm**: Project settings are pre-configured in `.idea/` (source roots automatically set)
- **VS Code**: Settings are pre-configured in `.vscode/settings.json` (includes pytest, ruff, pyright configuration)

## Quick Start

### Command Line

```bash
tui-delta
```

### Python API

```python
from tui-delta import TuiDelta

# Initialize with configuration
TEMPLATE_PLACEHOLDER = TuiDelta(
    TEMPLATE_PLACEHOLDER=TEMPLATE_PLACEHOLDER
)

# Process stream
with open("app.log") as infile, open("clean.log", "w") as outfile:
    for line in infile:
        TEMPLATE_PLACEHOLDER.TEMPLATE_PLACEHOLDER(TEMPLATE_PLACEHOLDER, outfile)
    TEMPLATE_PLACEHOLDER.flush(outfile)
```

## Use Cases

- **TEMPLATE_PLACEHOLDER** - TEMPLATE_PLACEHOLDER

## How It Works

`tui-delta` uses TEMPLATE_PLACEHOLDER:

1. **TEMPLATE_PLACEHOLDER** - TEMPLATE_PLACEHOLDER

TEMPLATE_PLACEHOLDER.

## Documentation

**[Read the full documentation at tui-delta.readthedocs.io](https://tui-delta.readthedocs.io/)**

Key sections:
- **Getting Started** - Installation and quick start guide
- **Use Cases** - Real-world examples across different domains
- **Guides** - TEMPLATE_PLACEHOLDER selection, performance tips, common patterns
- **Reference** - Complete CLI and Python API documentation

## Development

```bash
# Clone repository
git clone https://github.com/JeffreyUrban/tui-delta.git
cd tui-delta-workspace/tui-delta

# Install development dependencies
pip install -e ".[dev]"

# Complete initial project setup
# Prompt Claude Code: "Please perform Initial Project Kickoff"

# Run tests
pytest

# Run with coverage
pytest --cov=tui-delta --cov-report=html
```

### GitHub Repository Configuration

After creating your GitHub repository, run the configuration script to set up recommended settings:

```bash
./scripts/configure-github.sh
```

This script configures:
- **Merge strategy:** Squash and merge only (with other methods disabled)
- **Branch protection on main:**
  - Prevents force pushes and branch deletion
  - Enforces rules for administrators
  - Allows configuration of required status checks
- **Auto-delete branches** after merge
- **Auto-merge** capability

**Requirements:**
- [GitHub CLI](https://cli.github.com/) installed and authenticated (`gh auth login`)
- Admin permissions on the repository

The script will automatically detect your repository from the git remote, or you can specify it manually:

```bash
./scripts/configure-github.sh owner/repository-name
```

**Note:** After setting up GitHub Actions workflows, add required status checks by following the instructions shown at the end of the script output.

## Performance

- **Time complexity:** O(TEMPLATE_PLACEHOLDER)
- **Space complexity:** O(TEMPLATE_PLACEHOLDER)
- **Throughput:** TEMPLATE_PLACEHOLDER
- **Memory:** TEMPLATE_PLACEHOLDER

## License

MIT License - See [LICENSE](LICENSE) file for details

## Author

Jeffrey Urban

---

**[Star on GitHub](https://github.com/JeffreyUrban/tui-delta)** | **[Report Issues](https://github.com/JeffreyUrban/tui-delta/issues)**
