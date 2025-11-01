
from src.cd_command import cd

def test_cd(fs, base_path):
    """
    Проверяет работу функции cd
    """

    result = cd([f"{base_path}home/user"])
    assert result == "SUCCESS"

    result = cd(["../.."])
    assert result == "SUCCESS"

    result = cd(["home/user"])
    assert result == "SUCCESS"

    result = cd([f"{base_path}pam"])
    assert "не существует" in result

    result = cd([f"{base_path}home/user/laba.txt"])
    assert "не является директорией" in result

    result = cd([])
    assert "принимает ровно один аргумент" in result

    result = cd(["j", "g"])
    assert "принимает ровно один аргумент" in result

    result = cd([f"{base_path}\home"])
    assert result == "SUCCESS"

    result = cd([".."])
    assert result == "SUCCESS"

    result = cd(["."])
    assert result == "SUCCESS"
