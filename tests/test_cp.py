from src.cp_command import cp
from pathlib import Path

def test_cp(fs, base_path):
    """
    Проверяет работу функции cp
    """

    result = cp([f"{base_path}/home/user/laba.txt", f"{base_path}/tmp/laba.txt"])
    assert result == "SUCCESS"
    assert Path(f"{base_path}/tmp/laba.txt").exists()
    assert Path(f"{base_path}/home/user/laba.txt").exists()

    result = cp([f"{base_path}/home/user/project/infa.py", f"{base_path}/home/user/project/copy_infa.py"])
    assert result == "SUCCESS"
    assert Path(f"{base_path}/home/user/project/copy_infa.py").exists()
    assert Path(f"{base_path}/home/user/project/infa.py").exists()

    result = cp(["-r", f"{base_path}/home/user/project", f"{base_path}/tmp/project"])
    assert result == "SUCCESS"
    assert Path(f"{base_path}/tmp/project").exists()
    assert Path(f"{base_path}/tmp/project/infa.py").exists()
    assert Path(f"{base_path}/home/user/project").exists()

    result = cp([f"{base_path}/home/user/project", f"{base_path}/tmp"])
    assert "для копирования директории используйте флаг -r" in result

    result = cp([f"{base_path}/notexistent.txt", f"{base_path}/tmp"])
    assert "неправильный путь" in result

    result = cp(["-r", f"{base_path}/home/user", f"{base_path}/import.txt"])
    assert "невозможно скопировать директорию в файл" in result

    result = cp(["-r", f"{base_path}/home", f"{base_path}/home/user"])
    assert "невозможно скопировать директорию в саму себя" in result

    result = cp([f"{base_path}/home/user/laba.txt"])
    assert "неправильный синтаксис команды" in result

    result = cp([f"{base_path}/import.txt", f"{base_path}/home/user"])
    assert result == "SUCCESS"
    assert Path(f"{base_path}/home/user/import.txt").exists()
    assert Path(f"{base_path}/import.txt").exists()

    result = cp([f"{base_path}/home/user/laba.txt", f"{base_path}/home/user/import.txt"])
    assert result == "SUCCESS"
    assert Path(f"{base_path}/home/user/laba.txt").exists()
    assert Path(f"{base_path}/home/user/import.txt").exists()
