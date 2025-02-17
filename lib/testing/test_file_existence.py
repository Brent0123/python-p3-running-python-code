from pathlib import Path

def test_app_py_exists():
    assert Path("lib/app.py").exists()