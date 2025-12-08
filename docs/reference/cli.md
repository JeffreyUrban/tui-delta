# ⚠️ Template doc: Testing disabled ⚠️

# CLI Reference

Complete reference for the `tui-delta` command-line interface.

## Command Syntax

```bash
tui-delta [OPTIONS] [INPUT_FILE]
```

## Basic Usage

```bash
# TEMPLATE_PLACEHOLDER
tui-delta TEMPLATE_PLACEHOLDER
```

## Options Reference

### Core Options

#### `--TEMPLATE_PLACEHOLDER, -b`
**Type**: TEMPLATE_PLACEHOLDER
**Default**: TEMPLATE_PLACEHOLDER

TEMPLATE_PLACEHOLDER.

```bash
tui-delta --TEMPLATE_PLACEHOLDER
```

### Display Options

#### `--quiet, -q`
**Type**: Boolean
**Default**: False

Suppress statistics output to stderr.

```bash
tui-delta --quiet input.log
```

#### `--progress, -p`
**Type**: Boolean
**Default**: False

Show progress indicator (auto-disabled for pipes).

```bash
tui-delta --progress large-file.log
```

#### `--stats-format`
**Type**: String (table | json)
**Default**: table

Statistics output format: 'table' (Rich table) or 'json' (machine-readable).

```bash
tui-delta --stats-format json input.log
```

#### `--explain`
**Type**: Boolean
**Default**: False

Show explanations to stderr for why TEMPLATE_PLACEHOLDER.

Outputs diagnostic messages showing TEMPLATE_PLACEHOLDER decisions:
- When TEMPLATE_PLACEHOLDER
- Which TEMPLATE_PLACEHOLDER

```bash
# See all TEMPLATE_PLACEHOLDER decisions
tui-delta --explain input.log 2> explain.log

# Debug with quiet mode (only explanations, no stats)
tui-delta --explain --quiet input.log

# Validate TEMPLATE_PLACEHOLDER
tui-delta --explain --TEMPLATE_PLACEHOLDER input.log 2>&1 | grep EXPLAIN
```

Example output:
```
EXPLAIN: TEMPLATE_PLACEHOLDER
```

See [Explain Mode](../features/explain/explain.md) for detailed usage.

### Version Information

#### `--version`
**Type**: Boolean
**Default**: False

Show version and exit.

```bash
tui-delta --version
```

Example output:
```
tui-delta version 0.1.0
```

## Option Combinations

### Mutually Exclusive Options

- `--TEMPLATE_PLACEHOLDER` and `--TEMPLATE_PLACEHOLDER`: Use one or the other
- `--TEMPLATE_PLACEHOLDER` requires `--TEMPLATE_PLACEHOLDER`

## Examples

### TEMPLATE_PLACEHOLDER

```bash
# TEMPLATE_PLACEHOLDER
tui-delta TEMPLATE_PLACEHOLDER.log > output.log
```

## Statistics Output

### Table Format (Default)

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┓
┃ Metric                   ┃  Value ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━┩
│ TEMPLATE_PLACEHOLDER                     │   TEMPLATE_PLACEHOLDER │
└──────────────────────────┴────────┘
```

### JSON Format

```json
{
  "statistics": {
    "TEMPLATE_PLACEHOLDER": TEMPLATE_PLACEHOLDER
  }
}
```

## Exit Codes

- **0**: Success
- **1**: Error (invalid arguments, file not found, processing error)

## See Also

- [TuiDelta API](tui-delta.md) - Core TEMPLATE_PLACEHOLDER class
- [Basic Concepts](../getting-started/basic-concepts.md) - Understanding how tui-delta works
