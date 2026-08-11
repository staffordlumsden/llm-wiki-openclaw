from pathlib import Path
import subprocess, sys

ROOT = Path(__file__).resolve().parents[1]

def test_validator_passes():
    result = subprocess.run([sys.executable, str(ROOT/'scripts'/'validate.py')], capture_output=True, text=True)
    assert result.returncode == 0, result.stdout + result.stderr

def test_skills_have_distinct_names():
    assert "name: llm-wiki" in (ROOT/'SKILL.md').read_text()
    assert "name: wiki-query" in (ROOT/'profiles'/'wiki-query'/'SKILL.md').read_text()
