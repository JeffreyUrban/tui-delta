# CLI Reference

Complete command-line reference for `tui-delta`.

## Commands

### `tui-delta into`

Run a TUI application and pipe processed output into a file.

**Usage:**

```console
$ tui-delta into OUTPUT-FILE [OPTIONS] -- COMMAND...
```

**Arguments:**

- `OUTPUT-FILE` - Output file to write processed deltas (can be a named pipe)
- `COMMAND...` - The TUI command to run (e.g., `claude code`, `npm test`)

**Options:**

- `--profile`, `-p` TEXT - Clear rules profile (claude_code, generic, minimal, or custom)
- `--rules-file` FILE - Path to custom clear_rules.yaml file
- `--help`, `-h` - Show help message

**Examples:**

Basic usage with Claude Code:

```console
$ tui-delta into session.log --profile claude_code -- claude code
```

Use generic profile for other TUI apps:

```console
$ tui-delta into aider.log --profile generic -- aider
```

Custom rules file:

```console
$ tui-delta into output.log --rules-file my-rules.yaml -- ./myapp
```

Use a named pipe for post-processing:

```console
$ mkfifo /tmp/my-pipe
$ cat /tmp/my-pipe | other-tool > final.txt &
$ tui-delta into /tmp/my-pipe --profile claude_code -- claude
```

**Pipeline:**

The `into` command processes output through:

```
script → clear_lines → consolidate → uniqseq → cut → additional_pipeline
```

Where `additional_pipeline` is profile-specific (e.g., final uniqseq for claude_code).

### `tui-delta list-profiles`

List available clear rules profiles.

**Usage:**

```console
$ tui-delta list-profiles
```

**Example output:**

```console
$ tui-delta list-profiles
Available profiles:
  claude_code: Claude Code terminal UI (claude.ai/code)
  generic: Generic TUI with only universal rules
  minimal: Minimal - only base rule, no protections
```

## Profiles

### claude_code

Optimized for Claude Code terminal UI sessions.

**Features:**

- Preserves submitted user input (final occurrence)
- Normalizes dialog questions and choices
- Handles activity spinners
- Tracks thinking indicators
- Maintains scrollback output
- Deduplicates task progress updates
  - (keeping the last instance shown... e.g. generally the total token count for an action)

**Use when:** Logging Claude Code sessions

### generic

Basic processing for most TUI applications.

**Features:**

- Universal clear detection
- Blank line boundary protection
- No pattern normalization

**Use when:** Logging any TUI application, or as starting point for custom profiles

### minimal

Minimal processing with only base clear detection.

**Features:**

- Base clear count formula (N-1)
- No protections
- No pattern normalization

**Use when:** Debugging or maximum raw output

## Output

The `into` command writes processed output to the specified file:

```console
$ tui-delta into session.log --profile claude_code -- claude  # Save to file
```

For post-processing, use a named pipe:

```console
$ mkfifo /tmp/pipe
$ tui-delta into /tmp/pipe -- claude &
$ cat /tmp/pipe | your-tool > final.txt
```

## Exit Codes

- `0` - Success
- `1` - Error in pipeline stage
- TUI application's exit code is preserved

## Environment

### Terminal Size

The `script` command used by tui-delta respects terminal size. Set `COLUMNS` and `LINES` for consistent output:

```console
$ COLUMNS=120 LINES=40 tui-delta into s.log --profile claude_code -- claude
```

## Next Steps

- **[Quick Start](../getting-started/quick-start.md)** - Get started quickly
- **[Custom Profiles](../guides/custom-profiles.md)** - Create your own profiles
