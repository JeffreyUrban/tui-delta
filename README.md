# TUI Delta

## ⚠️ Early Development - Not Ready for Use

**This project is under active development and is not ready for production use.**

- APIs may change without notice
- Documentation is incomplete
- No releases published yet
- Not accepting contributions at this time

> - **Star/watch the repo to be notified when the first release is available.**

**Run a TUI application (AI assistant sessions, et al) with real-time delta processing for monitoring and logging. Supports Claude Code.**

Capture and log AI assistant interactive sessions efficiently, streaming all meaningfully different content exactly as shown in the terminal. Fully supports Claude Code; other AI assistants (Cline, Cursor, Aider) expected to work with profile customization. The pipeline removes screen control sequences, outputs ephemeral content, and deduplicates redundant output - creating clean, viewable logs suitable for real-time monitoring and archival.

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

### Logging a Claude Code Session

```bash
# Run Claude Code with tui-delta processing
tui-delta --profile claude_code -- claude code

# Output streams to stdout in real-time
# You can pipe to logging tools, tee to file, etc.
```

### View Captured Logs

Logs preserve the original terminal appearance and are viewable with standard tools:

```bash
# View with less (supports colors and formatting)
less -R session.log

# Follow in real-time
tui-delta --profile claude_code -- claude code | tee session.log

# Monitor with tail
tui-delta --profile claude_code -- claude code > session.log &
tail -f session.log
```

## Use Cases

- **AI Assistant Logging** - Capture Claude Code sessions (fully supported); others expected to work with custom profiles
- **Real-time Monitoring** - Stream processed output to monitoring tools while the session runs
- **TUI Development** - Debug terminal applications by seeing all content changes
- **Education** - Record and share AI-assisted coding sessions with clean, readable logs

## How It Works

`tui-delta` wraps TUI applications and processes their output through a pipeline:

1. **Capture** - Uses `script` to capture all terminal output including control sequences
2. **Clear Detection** - Identifies lines that were cleared/overwritten (common in TUI apps)
3. **Consolidation** - Outputs only meaningful changes, removing redundant redraws
4. **Deduplication** - Removes duplicate sequences using configurable patterns
5. **Streaming** - All output streams in real-time to stdout for immediate use

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

## Features

- **Profile-based Processing** - Pre-configured profiles for Claude Code, generic TUI apps, and minimal processing
- **Custom Profiles** - Define your own YAML profiles for different TUI applications
- **Real-time Streaming** - Output streams as the session runs, no buffering delays
- **Preserves Appearance** - Logs show content exactly as displayed in terminal
- **Efficient Deduplication** - Smart removal of redundant content while keeping ephemeral changes
- **Unix Pipeline Friendly** - Works with standard Unix tools (tee, grep, tail, etc.)

## License

MIT License - See [LICENSE](LICENSE) file for details

## Author

Jeffrey Urban

---

**[Star on GitHub](https://github.com/JeffreyUrban/tui-delta)** | **[Report Issues](https://github.com/JeffreyUrban/tui-delta/issues)**
