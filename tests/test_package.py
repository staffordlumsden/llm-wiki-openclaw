from pathlib import Path
import subprocess, sys

ROOT = Path(__file__).resolve().parents[1]

def test_validator_passes():
    result = subprocess.run([sys.executable, str(ROOT/'scripts'/'validate.py')], capture_output=True, text=True)
    assert result.returncode == 0, result.stdout + result.stderr

def test_skills_have_distinct_names():
    assert "name: llm-wiki" in (ROOT/'SKILL.md').read_text()
    assert "name: wiki-query" in (ROOT/'profiles'/'wiki-query'/'SKILL.md').read_text()


def test_frontmatter_descriptions_are_yaml_safe():
    for path in [ROOT/'SKILL.md', ROOT/'profiles'/'wiki-query'/'SKILL.md']:
        text = path.read_text(encoding='utf-8')
        head = text[4:].split("\n---\n", 1)[0]
        description = next(line for line in head.splitlines() if line.startswith("description:"))
        value = description.split(":", 1)[1].strip()
        assert value.startswith(('"', "'")) and value.endswith(('"', "'"))
