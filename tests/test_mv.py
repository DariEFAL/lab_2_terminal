from src.mv_command import mv
from pathlib import Path

def test_mv(fs, base_path):
    """
    Проверяет работу функции mv
    """

    result = mv([f"{base_path}/home/user/laba.txt", f"{base_path}/tmp/laba.txt"])
    assert result == "SUCCESS"
    assert Path(f"{base_path}/tmp/laba.txt").exists()
    assert not Path(f"{base_path}/home/user/laba.txt").exists()

    result = mv([f"{base_path}/home/user/project/infa.py", f"{base_path}/home/user/project/main.py"])
    assert result == "SUCCESS"
    assert Path(f"{base_path}/home/user/project/main.py").exists()
    assert not Path(f"{base_path}/home/user/project/infa.py").exists()

    result = mv([f"{base_path}/home/user/project", f"{base_path}/tmp/project"])
    assert result == "SUCCESS"
    assert Path(f"{base_path}/tmp/project").exists()
    assert Path(f"{base_path}/tmp/project/main.py").exists()
    assert not Path(f"{base_path}/home/user/project").exists()

    result = mv([f"{base_path}/notexistent.txt", f"{base_path}/tmp"])
    assert "файл или директория не существует" in result

    result = mv([f"{base_path}/home/user", f"{base_path}/import.txt"])
    assert "невозможно переместить директорию в файл" in result

    result = mv([f"{base_path}/home", f"{base_path}/home/user"])
    assert "невозможно переместить директорию в саму себя" in result

    result = mv([f"{base_path}/home"])
    assert "неправильный синтаксис команды" in result

    result = mv([f"{base_path}/file1.txt", f"{base_path}/file2.txt", f"{base_path}/file3.txt"])
    assert "неправильный синтаксис команды" in result

    result = mv(["import.txt", f"{base_path}/home/user"])
    assert result == "SUCCESS"
    assert Path(f"{base_path}/home/user/import.txt").exists()
    assert not Path(f"{base_path}/import.txt").exists()

    result = mv([f"{base_path}/home/user/import.txt", f"{base_path}/home/newfile.txt"])
    assert result == "SUCCESS"
    assert not Path(f"{base_path}/home/user/import.txt").exists()
    assert Path(f"{base_path}/home/newfile.txt").exists()

    result = mv([f"{base_path}/homeр/user", f"{base_path}/home"])
    assert "путь не существует" in result
