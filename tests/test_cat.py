from src.cat_command import cat

def test_cat(fs, base_path, capsys):
    """
    Проверяет работу функции cat
    """

    result = cat([f"{base_path}/home/user/laba.txt"])
    cap = capsys.readouterr()
    assert result == "SUCCESS"
    assert "лаба по питону" in cap.out

    result = cat([f"{base_path}/pum.txt"])
    assert "не существует" in result

    result = cat([f"{base_path}/home/user"])
    assert "не является файлом" in result

    result = cat(["import.txt"])
    cap = capsys.readouterr()
    assert result == "SUCCESS"
    assert "очень важно" in cap.out

    result = cat([])
    assert "принимает ровно один аргумент" in result
