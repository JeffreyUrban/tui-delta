# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

No unreleased changes yet.

---

## [0.1.0] - 2025-12-11

### Added

**Core Features:**
- Real-time TUI output capture with intelligent delta processing
- Support for wrapping AI assistant sessions (Claude Code, others with custom profiles)
- Built-in profiles: `claude_code`, `generic`, `minimal`
- Custom profile support via YAML configuration
- Pattern-based line clearing detection and consolidation
- Sequence-based clearing with follower pattern support
- Output diff mode for debugging (`--diff`)

**CLI Tools:**
- `tui-delta run` - Main command for wrapping TUI applications
- `tui-delta list-profiles` - List available profiles
- `clear-lines` - Standalone utility for processing cleared line markers
- `consolidate-clears` - Standalone utility for consolidating screen clears

**Documentation:**
- Comprehensive user documentation with MkDocs Material
- Quick start guide and installation instructions
- AI assistant logging use cases and examples
- Custom profile creation guide
- CLI reference documentation
- All code examples tested with Sybil

**Testing & Quality:**
- 87% test coverage with 282 unit tests
- Integration tests for state machine and CLI
- Property-based tests for invariants
- Oracle-based testing with reference implementations
- CI/CD with GitHub Actions
- Code quality: ruff (lint + format) + pyright (type checking)

**Developer Experience:**
- Python 3.9+ support (tested on 3.9, 3.14)
- Clean, typed Python codebase
- Rich terminal output for CLI
- Typer framework for user-friendly commands

### Technical Details

- Uses syslog-ng for efficient TUI output processing
- Pattern database (YAML) for clear marker detection
- Unified sequence processing for multiple clear patterns
- Smart delta extraction preserving all meaningful content

Special thanks to the Python community and the developers of the excellent tools that made this project possible.

---

## Release Process

Releases are automated via GitHub Actions when a version tag is pushed:

1. Update CHANGELOG.md with release notes
2. Create and push Git tag: `git tag v0.1.0 && git push origin v0.1.0`
3. GitHub Actions automatically:
   - Creates GitHub Release
   - Publishes to PyPI (when configured)
4. Version number is automatically derived from Git tag

[Unreleased]: https://github.com/JeffreyUrban/tui-delta/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/JeffreyUrban/tui-delta/releases/tag/v0.1.0
