from pathlib import Path
from src.ls_command import ls

def test_ls(fs, base_path, capsys):
    """
    Проверяет работу функции ls
    """

    current_path = Path(f"{base_path}home/user")

    result = ls([], current_path)
    cap = capsys.readouterr()
    assert result == "SUCCESS"
    assert "laba.txt" in cap.out
    assert "project" in cap.out

    result = ls(["-l", "-l"], current_path)
    cap = capsys.readouterr()
    assert result == "SUCCESS"
    assert "-" in cap.out

    fs.create_dir(f"{base_path}something")
    result = ls(["something"], current_path)
    cap = capsys.readouterr()
    assert result == "SUCCESS"
    assert "something" in cap.out

    result = ls([f"{base_path}home/user/project"], current_path)
    cap = capsys.readouterr()
    assert result == "SUCCESS"
    assert "project" in cap.out
    assert "infa.py" in cap.out

    result = ls([f"{base_path}home/user/project", "-l"], current_path)
    cap = capsys.readouterr()
    assert result == "SUCCESS"
    assert "project" in cap.out
    assert "infa.py" in cap.out
    assert "-" in cap.out

    result = ls([f"{base_path}pam"], current_path)
    assert "не существует" in result

    result = ls([f"{base_path}home/user/laba.txt"], current_path)
    cap = capsys.readouterr()
    assert result == "SUCCESS"
    assert "user" in cap.out
    assert "laba.txt" in cap.out
