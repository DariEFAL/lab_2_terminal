from src.zip_command import zip
from pathlib import Path

def test_zip(fs, base_path):
    """
    Проверяет работу функции zip
    """

    result = zip([f"{base_path}/home/user", f"{base_path}/user.zip"])
    assert result == "SUCCESS"
    assert Path(f"{base_path}/user.zip").exists()

    result = zip([f"{base_path}/home/user/laba.txt", f"{base_path}/laba.zip"])
    assert result == "SUCCESS"
    assert Path(f"{base_path}/laba.zip").exists()

    result = zip([f"{base_path}/home/user"])
    assert "неправильный синтаксис команды" in result

    result = zip([f"{base_path}/home/user", f"{base_path}/user"])
    assert "укажите расширение .zip" in result

    result = zip([f"{base_path}/home/user", f"{base_path}/user.tar"])
    assert "укажите расширение .zip" in result

    result = zip([f"{base_path}/not", f"{base_path}/pum.zip"])
    assert "исходный путь не существует" in result

    result = zip([f"{base_path}/home/user", f"{base_path}/home/user/pum.zip"])
    assert "запрещено архивировать папку в саму себя" in result

    result = zip([f"{base_path}/home/user", f"{base_path}/tmp/user.zip"])
    assert result == "SUCCESS"
    assert Path(f"{base_path}/tmp/user.zip").exists()
