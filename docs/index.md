# tui-delta

**Run a TUI application with real-time delta processing for monitoring and logging AI assistant sessions**

`tui-delta` captures and logs AI assistant interactive sessions efficiently, streaming all meaningfully different content exactly as shown in the terminal.

## Primary Use Case

Log AI assistant sessions (Claude Code, Cline, Cursor, Aider, etc.) with:

- **Real-time streaming** - Monitor sessions as they run
- **Clean output** - Removes screen control sequences and redundant redraws
- **Preserves appearance** - Logs viewable with `less` or `less -R` (system-dependent) show original formatting
- **Efficient capture** - Outputs all ephemeral content while deduplicating redundant output

## Quick Example

```console
$ tui-delta --profile claude_code -- claude code > session.log
```

This wraps Claude Code, processes its output in real-time, and saves to `session.log` while displaying to terminal.

## How It Works

1. **Wraps TUI application** using `script` to capture all terminal output
2. **Detects cleared lines** - Identifies content that was overwritten
3. **Consolidates changes** - Outputs only meaningful differences
4. **Deduplicates sequences** - Removes redundant output using profile-specific patterns
5. **Streams to stdout** - All output available immediately for piping or logging

## Features

- **Profile-based Processing** - Pre-configured for Claude Code, plus support for user-specified profiles
- **Custom Profiles** - Define YAML profiles for other TUI applications
- **Real-time Streaming** - No unnecessary delays, output streams as session runs
- **Unix Pipeline Friendly** - Works with standard command-line tools and logging software

## Getting Started

- [Installation](getting-started/installation.md) - Install tui-delta
- [Quick Start](getting-started/quick-start.md) - Log your first AI assistant session
- [Basic Concepts](getting-started/basic-concepts.md) - Understand how tui-delta works

## Documentation Sections

- **[Getting Started](getting-started/installation.md)** - Installation and quick start
- **[Use Cases](use-cases/ai-assistants/ai-assistants.md)** - Real-world applications
- **[Guides](guides/common-patterns.md)** - How-to guides and patterns
- **[Reference](reference/cli.md)** - CLI and Python API documentation
- **[About](about/algorithm.md)** - Algorithm details and design decisions
