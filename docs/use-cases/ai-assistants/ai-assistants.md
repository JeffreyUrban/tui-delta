# Logging AI Assistant Sessions

Primary use case: capturing and logging AI assistant interactive sessions.

## AI Assistant Compatibility

- **Claude Code** - Fully supported with optimized profile
- **Cline, Cursor, Aider** - Expected to work; likely requires profile customization for best results
- **Other AI assistant TUIs** - Should work with `generic` profile or custom profile

**Note:** Only Claude Code is officially supported. Other assistants are expected to work but may need custom profiles for optimal results. Community contributions welcome.

## Claude Code Sessions

### Basic Logging

```console
$ tui-delta run --profile claude_code -- claude code > session.log
```

Captures the full session with:

- User prompts and assistant responses
- Tool use (file reads, writes, commands)
- Ephemeral content (spinners, progress indicators)
- Dialog interactions

### Real-time Monitoring + Logging

```console
$ tui-delta run --profile claude_code -- claude code | tee session.log
```

Display in terminal AND save to file simultaneously.

### Review Logged Session

```console
$ less -R session.log
```

The `-R` flag preserves ANSI colors and formatting.

## Other AI Assistants

Start with the `generic` profile:

```console
$ tui-delta run --profile generic -- aider
$ tui-delta run --profile generic -- cursor
$ tui-delta run --profile generic -- cline
```

For best results, you'll likely need to create a custom profile. See [Custom Profiles](../../guides/custom-profiles.md).

**Community contributions:** We welcome profile contributions for other AI assistants!

## Use Cases

### Session Archival

Keep records of AI-assisted development sessions:

```console
$ tui-delta run --profile claude_code -- claude code > "session-$(date +%Y%m%d-%H%M%S).log"
```

Creates timestamped log files for each session.

### Review and Learning

Review past sessions to:

- Understand what changes were made
- Learn from assistant's suggestions
- Document project decisions
- Share examples with team

### Debugging

When unexpected behavior occurs:

```console
$ tui-delta run --profile claude_code -- claude code 2>&1 | tee full-session.log
```

Captures both stdout and stderr for debugging.

## Log Format

Logged sessions:

- Preserve original terminal appearance
- Include all meaningful content changes
- Remove redundant screen redraws
- Viewable with standard Unix tools (`less`, `grep`, etc.)

## Integration with Logging Tools

### Append to Daily Log

```console
$ tui-delta run --profile claude_code -- claude code >> daily-$(date +%Y%m%d).log
```

### Pipe to Analysis Tools

```console
$ tui-delta run --profile claude_code -- claude code | grep -i "error"
```

### Stream to Remote Logging

```console
$ tui-delta run --profile claude_code -- claude code | logger -t claude-code
```

## Next Steps

- **[Quick Start](../../getting-started/quick-start.md)** - Get started quickly
- **[Custom Profiles](../../guides/custom-profiles.md)** - Create profiles for other assistants
