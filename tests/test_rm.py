from src.rm_command import rm
from pathlib import Path


def test_rm_success(fs, base_path):
    """
    Проверяет работу функции rm с правильным вводом
    """

    result = rm([f"{base_path}/home/user/laba.txt"], Path(f"{base_path}"))
    assert result == "SUCCESS"
    assert not Path(f"{base_path}/home/user/laba.txt").exists()

    result = rm(["import.txt"], Path(f"{base_path}"))
    assert result == "SUCCESS"
    assert not Path(f"{base_path}/import.txt").exists()

def test_rm_error(fs, base_path):
    """
    Проверяет работу функции rm с ошибочным вводом
    """

    result = rm([f"{base_path}/home/user/project"], Path(f"{base_path}"))
    assert "для удаления директории используйте флаг -r" in result
    assert Path(f"{base_path}/home/user/project").exists()

    result = rm([f"{base_path}/notexistent.txt"], Path(f"{base_path}"))
    assert "не является файлом или директорией" in result

    result = rm([], Path(f"{base_path}"))
    assert "неправильный синтаксис команды" in result

    result = rm([f"{base_path}/file1.txt", f"{base_path}/file2.txt"], Path(f"{base_path}"))
    assert "неправильный синтаксис команды" in result

    result = rm(["-r", f"{base_path}"], Path(f"{base_path}"))
    assert "запрещено удалять корневой каталог" in result

def test_rm_input(fs, base_path, monkeypatch):
    """Проверка подтверждения удаления катологов"""

    monkeypatch.setattr('builtins.input', lambda _: "n")

    result = rm(["-r", f"{base_path}/home/user/project"], Path(f"{base_path}"))
    assert "удаление отменено пользователем" in result
    assert Path(f"{base_path}/home/user/project").exists()

    monkeypatch.setattr('builtins.input', lambda _: "y")

    result = rm(["-r", f"{base_path}/home/user/project"], Path(f"{base_path}"))
    assert result == "SUCCESS"
    assert not Path(f"{base_path}/home/user/project").exists()
