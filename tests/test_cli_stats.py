"""Tests for CLI statistics printing."""

import pytest

from tui_delta.cli import print_stats
from tui_delta.tui_delta import TuiDelta


@pytest.mark.unit
def test_print_stats_normal():
    """Test print_stats with normal processor."""
    processor = TuiDelta()

    # print_stats writes to stderr via rich Console
    # Just verify it doesn't crash
    print_stats(processor)


@pytest.mark.unit
def test_print_stats_empty():
    """Test print_stats with no lines processed."""
    processor = TuiDelta()

    # print_stats should handle empty stats
    print_stats(processor)
