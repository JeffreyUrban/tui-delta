"""Unit tests for consolidate_clears.py helper functions."""

import io

import pytest
from rich.console import Console
from rich.text import Text


@pytest.mark.unit
class TestCharDiff:
    """Test _char_diff function with various inputs."""

    def test_char_diff_equal_strings(self):
        """Test _char_diff with identical strings."""
        from tui_delta.consolidate_clears import _char_diff

        result = _char_diff("hello world", "hello world")

        # Should return Text object
        assert isinstance(result, Text)
        # Content should match
        assert "hello world" in str(result)

    def test_char_diff_completely_different(self):
        """Test _char_diff with completely different strings."""
        from tui_delta.consolidate_clears import _char_diff

        result = _char_diff("abc", "xyz")

        assert isinstance(result, Text)
        # Should show differences
        assert len(str(result)) > 0

    def test_char_diff_empty_strings(self):
        """Test _char_diff with empty strings."""
        from tui_delta.consolidate_clears import _char_diff

        result = _char_diff("", "")

        assert isinstance(result, Text)

    def test_char_diff_one_empty(self):
        """Test _char_diff with one empty string."""
        from tui_delta.consolidate_clears import _char_diff

        result1 = _char_diff("text", "")
        result2 = _char_diff("", "text")

        assert isinstance(result1, Text)
        assert isinstance(result2, Text)

    def test_char_diff_partial_match(self):
        """Test _char_diff with partial match."""
        from tui_delta.consolidate_clears import _char_diff

        result = _char_diff("hello world", "hello there")

        assert isinstance(result, Text)
        # Should have both matching and different parts
        assert "hello" in str(result)


@pytest.mark.unit
class TestRenderComponentSequence:
    """Test _render_component_sequence function."""

    def test_render_empty_components(self):
        """Test rendering empty component list."""
        from tui_delta.consolidate_clears import _render_component_sequence

        result = _render_component_sequence([])

        assert result == ""

    def test_render_text_only_components(self):
        """Test rendering text-only components."""
        from tui_delta.consolidate_clears import _render_component_sequence

        components = [{"text": "hello"}, {"text": " "}, {"text": "world"}]

        result = _render_component_sequence(components)

        assert "hello" in result
        assert "world" in result

    def test_render_with_serialized_field(self):
        """Test rendering with serialized field."""
        from tui_delta.consolidate_clears import _render_component_sequence

        # When both text and serialized present, text takes precedence
        components = [
            {"serialized": "123"}  # Only serialized, no text
        ]

        result = _render_component_sequence(components)

        assert "123" in result

    def test_render_mixed_components(self):
        """Test rendering mixed text and serialized."""
        from tui_delta.consolidate_clears import _render_component_sequence

        components = [{"text": "count: "}, {"text": "5", "serialized": "5"}, {"text": " items"}]

        result = _render_component_sequence(components)

        assert "count" in result
        assert "5" in result
        assert "items" in result


@pytest.mark.unit
class TestPrintPrefixedLine:
    """Test _print_prefixed_line function."""

    def test_print_prefixed_line_basic(self, capsys):
        """Test _print_prefixed_line with basic input."""
        from tui_delta.consolidate_clears import _print_prefixed_line

        _print_prefixed_line("+: ", "test content", None)

        captured = capsys.readouterr()
        assert "+: test content" in captured.out

    def test_print_prefixed_line_with_console(self):
        """Test _print_prefixed_line with Rich console."""
        from tui_delta.consolidate_clears import _print_prefixed_line

        buffer = io.StringIO()
        console = Console(file=buffer, force_terminal=False)

        _print_prefixed_line("+: ", "test content", console)

        output = buffer.getvalue()
        assert "test content" in output

    def test_print_prefixed_line_empty_content(self, capsys):
        """Test _print_prefixed_line with empty content."""
        from tui_delta.consolidate_clears import _print_prefixed_line

        _print_prefixed_line("+: ", "", None)

        captured = capsys.readouterr()
        assert "+: " in captured.out

    def test_print_prefixed_line_text_object(self, capsys):
        """Test _print_prefixed_line with Text object."""
        from tui_delta.consolidate_clears import _print_prefixed_line

        text = Text("styled text")
        _print_prefixed_line("+: ", text, None)

        captured = capsys.readouterr()
        assert "styled text" in captured.out


@pytest.mark.unit
class TestNormalize:
    """Test normalize function."""

    def test_normalize_with_none_engine(self):
        """Test normalize with None engine."""
        from tui_delta.consolidate_clears import normalize

        lines = ["line1", "line2", "line3"]
        result = normalize(None, lines)

        # Should return original lines unchanged
        assert result == lines

    def test_normalize_with_empty_list(self):
        """Test normalize with empty list."""
        from tui_delta.consolidate_clears import normalize

        result = normalize(None, [])

        assert result == []


@pytest.mark.unit
class TestParseLine:
    """Test parse_line edge cases."""

    def test_parse_line_kept(self):
        """Test parse_line with kept prefix."""
        from tui_delta.consolidate_clears import LineType, parse_line

        line_type, content = parse_line("+: some content")

        assert line_type == LineType.KEPT
        assert content == "some content"

    def test_parse_line_cleared_backslash(self):
        """Test parse_line with backslash cleared prefix."""
        from tui_delta.consolidate_clears import LineType, parse_line

        line_type, content = parse_line("\\: cleared content")

        assert line_type == LineType.CLEARED_BACKSLASH
        assert content == "cleared content"

    def test_parse_line_cleared_slash(self):
        """Test parse_line with forward slash cleared prefix."""
        from tui_delta.consolidate_clears import LineType, parse_line

        line_type, content = parse_line("/: cleared content")

        assert line_type == LineType.CLEARED_SLASH
        assert content == "cleared content"

    def test_parse_line_command(self):
        """Test parse_line with command prefix."""
        from tui_delta.consolidate_clears import LineType, parse_line

        line_type, content = parse_line(">: [window-title:test]")

        assert line_type == LineType.COMMAND
        assert content == "[window-title:test]"

    def test_parse_line_invalid_prefix(self):
        """Test parse_line with invalid prefix raises error."""
        from tui_delta.consolidate_clears import parse_line

        with pytest.raises(ValueError, match="Unrecognized line prefix"):
            parse_line("invalid prefix")

    def test_parse_line_empty_content(self):
        """Test parse_line with empty content after prefix."""
        from tui_delta.consolidate_clears import LineType, parse_line

        line_type, content = parse_line("+: ")

        assert line_type == LineType.KEPT
        assert content == ""


@pytest.mark.unit
class TestIsWindowTitleLine:
    """Test is_window_title_line function."""

    def test_is_window_title_true(self):
        """Test is_window_title_line with window title."""
        from tui_delta.consolidate_clears import is_window_title_line

        assert is_window_title_line("[window-title:test]") is True

    def test_is_window_title_icon_true(self):
        """Test is_window_title_line with window title icon."""
        from tui_delta.consolidate_clears import is_window_title_line

        assert is_window_title_line("[window-title-icon:test]") is True

    def test_is_window_title_false(self):
        """Test is_window_title_line with non-window-title."""
        from tui_delta.consolidate_clears import is_window_title_line

        assert is_window_title_line("regular content") is False

    def test_is_window_title_empty(self):
        """Test is_window_title_line with empty string."""
        from tui_delta.consolidate_clears import is_window_title_line

        assert is_window_title_line("") is False


@pytest.mark.unit
class TestCreateRulesFile:
    """Test _create_rules_file_from_profiles function."""

    def test_create_rules_file_returns_path(self):
        """Test that _create_rules_file_from_profiles returns a Path."""
        from pathlib import Path

        from tui_delta.consolidate_clears import _create_rules_file_from_profiles

        result = _create_rules_file_from_profiles()

        assert isinstance(result, Path)
        # Should be a temporary file
        assert result.exists()
        # Cleanup
        result.unlink()

    def test_create_rules_file_has_content(self):
        """Test that created rules file has content."""
        from tui_delta.consolidate_clears import _create_rules_file_from_profiles

        result = _create_rules_file_from_profiles()

        # Should have content (copied from tui_profiles.yaml)
        content = result.read_text()
        assert len(content) > 0
        # Should contain YAML structure
        assert "profiles:" in content or "rules:" in content or "patterns:" in content

        # Cleanup
        result.unlink()


@pytest.mark.unit
class TestOutputDiff:
    """Test output_diff function with various scenarios."""

    def test_output_diff_returns_sequence_lines(self):
        """Test output_diff returns sequence lines."""
        from tui_delta.consolidate_clears import output_diff

        result = output_diff(["line1"], ["line1"], "\\: ")

        # Should return a list
        assert isinstance(result, list)

    def test_output_diff_different_lines(self):
        """Test output_diff with different lines."""
        from tui_delta.consolidate_clears import output_diff

        result = output_diff(["old"], ["new"], "\\: ")

        assert isinstance(result, list)

    def test_output_diff_empty_old(self):
        """Test output_diff with empty old lines."""
        from tui_delta.consolidate_clears import output_diff

        result = output_diff([], ["new line"], "\\: ")

        assert isinstance(result, list)

    def test_output_diff_empty_new(self):
        """Test output_diff with empty new lines."""
        from tui_delta.consolidate_clears import output_diff

        result = output_diff(["old line"], [], "\\: ")

        assert isinstance(result, list)

    def test_output_diff_multiline(self):
        """Test output_diff with multiline."""
        from tui_delta.consolidate_clears import output_diff

        old = ["line1", "line2", "line3"]
        new = ["line1", "line2", "line3"]

        result = output_diff(old, new, "\\: ")

        assert isinstance(result, list)
