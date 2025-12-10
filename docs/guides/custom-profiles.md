# Custom Profiles

Create custom profiles for your TUI applications.

## Profile Structure

Profiles are defined in YAML files with three main sections:

```yaml
profiles:
  my_profile:
    description: "My TUI application"
    clear_protections:
      - blank_boundary
    normalization_patterns:
      - my_pattern
    additional_pipeline: "uniqseq --track '^\\S' --quiet"
```

## Creating a Custom Profile

### 1. Create a YAML File

Create `my-profiles.yaml`:

```yaml
profiles:
  my_app:
    description: "My TUI application"
    clear_protections:
      - blank_boundary
    normalization_patterns: []
```

### 2. Use with `--rules-file`

```console
$ tui-delta run --rules-file my-profiles.yaml -- ./myapp
```

## Profile Fields

### `description`

Human-readable description shown in `list-profiles`.

### `clear_protections`

List of protection rules to apply. Available protections:

- **`blank_boundary`** - Preserve blank lines at clear boundaries
- **`user_input_final`** - Preserve final user input (Claude Code specific)

Start with `blank_boundary` for most TUI apps.

### `normalization_patterns`

List of pattern names to normalize during consolidation. Patterns make lines with varying details (timestamps, spinners) compare as equal.

For most TUIs, start with empty list `[]`.

### `additional_pipeline`

Optional shell command for final processing. Common use:

```yaml
additional_pipeline: "uniqseq --track '^\\S' --quiet"
```

This adds a final deduplication stage.

## Example: Starting from Generic

Copy the `generic` profile as a template:

```yaml
profiles:
  my_custom:
    description: "My custom profile"
    clear_protections:
      - blank_boundary
    normalization_patterns: []
```

Test it:

```console
$ tui-delta run --rules-file my-custom.yaml --profile my_custom -- ./myapp
```

## Defining Patterns (Advanced)

Normalization patterns define how to recognize and normalize lines. Example:

```yaml
patterns:
  my_spinner:
    description: "Spinner with rotating symbols"
    pattern:
      - char: "·✢✳✶✻✽"  # Matches any of these symbols
      - text: " "
      - field: task
      - text: "…"
    output: "[spinner:{task}]"
```

This normalizes all spinner variations to `[spinner:task_name]` for comparison.

See `src/tui_delta/tui_profiles.yaml` for complete pattern examples.

## Testing Your Profile

1. Run on sample session:
   ```console
   $ tui-delta run --rules-file my-profile.yaml -- ./myapp | less -R
   ```

2. Check output looks correct
3. Adjust protections or patterns as needed

## Next Steps

- **[CLI Reference](../reference/cli.md)** - Command options
- **[tui_profiles.yaml](https://github.com/JeffreyUrban/tui-delta/blob/main/src/tui_delta/tui_profiles.yaml)** - Built-in profile examples
