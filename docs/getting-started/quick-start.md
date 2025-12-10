# Quick Start

Get started with `tui-delta` in 5 minutes.

## Installation

```bash
pip install tui-delta
```

## Basic Usage

### Log an AI Assistant Session

The primary use case - wrap Claude Code and capture the session:

```console
$ tui-delta run --profile claude_code -- claude code > session.log
```

This:

1. Runs Claude Code normally (you can interact with it)
2. Captures all terminal output
3. Processes it to remove duplicates and cleared lines
4. Streams clean output to `session.log`

### View the Log

Logs preserve terminal formatting:

```console
$ less -R session.log
```

The `-R` flag preserves colors and formatting.

## Common Patterns

### Save and Display Simultaneously

```console
$ tui-delta run --profile claude_code -- claude code | tee session.log
```

Streams to both stdout (your terminal) and `session.log`.

### Real-time Monitoring

```console
$ tui-delta run --profile claude_code -- claude code > session.log &
$ tail -f session.log
```

Run in background and monitor with `tail`.

### Use with Other AI Assistants

Other AI assistants expected to work but likely need profile customization:

```console
$ tui-delta run --profile generic -- aider
$ tui-delta run --profile generic -- cursor
```

Start with `generic` profile, then customize as needed. See [Custom Profiles](../guides/custom-profiles.md).

## Available Profiles

List installed profiles:

```console
$ tui-delta list-profiles
Available profiles:
  claude_code: Claude Code terminal UI (claude.ai/code)
  generic: Generic TUI with only universal rules
  minimal: Minimal - only base rule, no protections
```

## Next Steps

- **[Basic Concepts](basic-concepts.md)** - Understand how tui-delta works
- **[CLI Reference](../reference/cli.md)** - Complete command-line options
- **[Custom Profiles](../guides/custom-profiles.md)** - Create profiles for your TUI apps
