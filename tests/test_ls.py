from pathlib import Path
from src.ls_command import ls

def test_ls(fs, base_path, capsys):
    #Тест ls без аргументов (текущая директория) и только с -l

    current_path = Path(f"{base_path}home/user")

    result = ls([], current_path)
    captured = capsys.readouterr()
    assert result == "SUCCESS"
    assert "file1.txt" in captured.out
    assert "subdir" in captured.out

    result = ls(["-l", "-l"], current_path)
    captured = capsys.readouterr()
    assert result == "SUCCESS"
    assert "-" in captured.out

    #Тест ls с указанием конкретной папки
    current_path = Path(f"{base_path}home/user")

    fs.create_dir(f"{base_path}subdir")
    result = ls(["subdir"], current_path)
    captured = capsys.readouterr()
    assert result == "SUCCESS"
    assert "subdir" in captured.out

    result = ls([f"{base_path}home/user/subdir"], current_path)
    captured = capsys.readouterr()
    assert result == "SUCCESS"
    assert "subdir" in captured.out
    assert "file2.txt" in captured.out

    # Тест ls с указанием конкретной папки c -l
    current_path = Path(f"{base_path}home/user")

    result = ls([f"{base_path}home/user", "-l"], current_path)
    captured = capsys.readouterr()
    assert result == "SUCCESS"
    assert "user" in captured.out
    assert "file1.txt" in captured.out
    assert "subdir" in captured.out
    assert "-" in captured.out

    # Тест ls с несуществующей директорией
    current_path = Path(f"{base_path}home/user")

    result = ls([f"{base_path}subdir1"], current_path)
    assert "не существует" in result

    # Тест ls когда передаем файл вместо папки
    current_path = Path(f"{base_path}home/user")

    result = ls([f"{base_path}home/user/file1.txt"], current_path)
    captured = capsys.readouterr()
    assert result == "SUCCESS"
    assert "user" in captured.out
    assert "file1.txt" in captured.out
