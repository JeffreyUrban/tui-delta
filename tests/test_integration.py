"""Integration tests for end-to-end Claude Code pipeline."""

import subprocess
import sys
from pathlib import Path

import pytest

from tui_delta.run import run_tui_with_pipeline, build_pipeline_commands

# Path to test fixtures
FIXTURES_DIR = Path(__file__).parent / "fixtures"
REAL_CLAUDE_SESSION = FIXTURES_DIR / "real-claude-session.bin"


@pytest.mark.integration
class TestClaudeCodePipeline:
    """Integration tests with real Claude Code session data."""

    @pytest.fixture
    def mock_tui_command(self, tmp_path):
        """Create a mock TUI command that outputs the real Claude session data."""
        mock_script = tmp_path / "mock_claude.py"
        mock_script.write_text(f'''#!/usr/bin/env python3
import sys
fixture_path = r"{REAL_CLAUDE_SESSION}"
with open(fixture_path, "rb") as f:
    sys.stdout.buffer.write(f.read())
''')
        mock_script.chmod(0o755)
        return [sys.executable, str(mock_script)]

    def test_full_pipeline_with_run_function(self, mock_tui_command, tmp_path):
        """Test complete pipeline using run_tui_with_pipeline function.

        This tests the actual integration - the run.py module building and
        executing the pipeline, not manual subprocess wiring.
        """
        if not REAL_CLAUDE_SESSION.exists():
            pytest.skip(f"Real Claude Code session fixture not found: {REAL_CLAUDE_SESSION}")

        output_file = tmp_path / "output.txt"

        # Capture stdout by redirecting in subprocess
        test_script = tmp_path / "test_runner.py"
        test_script.write_text(f'''
import sys
sys.path.insert(0, r"{Path(__file__).parent.parent / 'src'}")
from tui_delta.run import run_tui_with_pipeline

exit_code = run_tui_with_pipeline(
    command={mock_tui_command},
    profile="claude_code",
)
sys.exit(exit_code)
''')

        result = subprocess.run(
            [sys.executable, str(test_script)],
            capture_output=True,
            timeout=60,
        )

        # Verify pipeline completed successfully
        assert result.returncode == 0, f"Pipeline failed: {result.stderr.decode()}"

        # Verify we got output
        output = result.stdout
        assert len(output) > 0, "Pipeline produced no output"

        # Verify output is reasonable (not just whitespace)
        lines = output.decode('utf-8', errors='replace').strip().split('\n')
        non_empty_lines = [line for line in lines if line.strip()]
        assert len(non_empty_lines) > 0, "Pipeline produced only empty lines"

        # Verify output is significantly smaller than input (compression from deduplication)
        input_size = REAL_CLAUDE_SESSION.stat().st_size
        assert len(output) < input_size, \
            f"Pipeline output ({len(output)}) should be smaller than input ({input_size})"

    def test_pipeline_commands_structure(self):
        """Test that build_pipeline_commands returns the correct pipeline structure."""
        pipeline = build_pipeline_commands(profile="claude_code")

        # Should have 5 stages: clear_lines, consolidate, uniqseq, cut, final uniqseq
        assert len(pipeline) == 5, f"Expected 5 pipeline stages, got {len(pipeline)}"

        # Stage 1: clear_lines
        assert "clear_lines" in " ".join(pipeline[0])
        assert "--prefixes" in pipeline[0]
        assert "--profile" in pipeline[0]
        assert "claude_code" in pipeline[0]

        # Stage 2: consolidate_clears
        assert "consolidate_clears" in " ".join(pipeline[1])

        # Stage 3: first uniqseq
        assert "uniqseq" in " ".join(pipeline[2])
        assert "--track" in pipeline[2]

        # Stage 4: cut (Python one-liner)
        assert "print(line[3:])" in " ".join(pipeline[3])

        # Stage 5: additional_pipeline from claude_code profile (final uniqseq)
        assert "uniqseq" in " ".join(pipeline[4])

    def test_pipeline_output_quality(self, mock_tui_command, tmp_path):
        """Test that pipeline output is clean and readable."""
        if not REAL_CLAUDE_SESSION.exists():
            pytest.skip(f"Real Claude Code session fixture not found: {REAL_CLAUDE_SESSION}")

        test_script = tmp_path / "test_runner.py"
        test_script.write_text(f'''
import sys
sys.path.insert(0, r"{Path(__file__).parent.parent / 'src'}")
from tui_delta.run import run_tui_with_pipeline

run_tui_with_pipeline(
    command={mock_tui_command},
    profile="claude_code",
)
''')

        result = subprocess.run(
            [sys.executable, str(test_script)],
            capture_output=True,
            timeout=60,
        )

        output_text = result.stdout.decode('utf-8', errors='replace')
        lines = output_text.strip().split('\n')

        # Quality checks
        # Should have removed most ANSI escape sequences (some remain in normalized patterns)
        ansi_heavy_lines = [line for line in lines if line.count('\x1b[') > 3]
        ansi_ratio = len(ansi_heavy_lines) / max(len(lines), 1)
        assert ansi_ratio < 0.2, f"Too many lines ({ansi_ratio:.1%}) with heavy ANSI escape sequences"

        # Should not have state prefixes (cut should remove them)
        prefixed_lines = [line for line in lines if line.startswith(('+: ', '\\: ', '/: ', '>: '))]
        assert len(prefixed_lines) == 0, "Output should not contain state prefixes after cut"

        # Should have reasonable line length distribution
        avg_line_length = sum(len(line) for line in lines) / max(len(lines), 1)
        assert avg_line_length < 500, f"Average line length ({avg_line_length:.0f}) too high"


@pytest.mark.integration
class TestGenericProfile:
    """Integration tests with generic profile."""

    def test_generic_profile_pipeline(self):
        """Test pipeline structure with generic profile."""
        pipeline = build_pipeline_commands(profile="generic")

        # Generic should have 4 stages (no additional_pipeline)
        # clear_lines, consolidate, uniqseq, cut
        assert len(pipeline) == 4, f"Expected 4 pipeline stages for generic, got {len(pipeline)}"


@pytest.mark.integration
class TestProfileSystem:
    """Integration tests for profile system."""

    def test_list_profiles_cli(self):
        """Test listing available profiles via CLI."""
        result = subprocess.run(
            [sys.executable, "-m", "tui_delta.cli", "list-profiles"],
            capture_output=True,
            text=True,
        )

        assert result.returncode == 0
        # CLI uses rich console which outputs to stderr
        output = result.stdout + result.stderr
        assert "claude_code" in output
        assert "generic" in output
        assert "minimal" in output

    def test_profile_descriptions(self):
        """Verify profiles have descriptions."""
        result = subprocess.run(
            [sys.executable, "-m", "tui_delta.cli", "list-profiles"],
            capture_output=True,
            text=True,
        )

        # Should show descriptions, not just names
        # CLI uses rich console which outputs to stderr
        output = result.stdout + result.stderr
        assert "Claude Code" in output or "terminal UI" in output
