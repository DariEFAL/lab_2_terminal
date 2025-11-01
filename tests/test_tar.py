from src.tar_command import tar


def test_tar(fs, base_path):
    """
    Проверяет работу функции tar
    """

    result = tar([f"{base_path}/home/user"])
    assert "неправильный синтаксис команды" in result

    result = tar([f"{base_path}/home/user", f"{base_path}/user"])
    assert "укажите расширение .tar.gz" in result

    result = tar([f"{base_path}/home/user", f"{base_path}/user.zip"])
    assert "укажите расширение .tar.gz" in result

    result = tar([f"{base_path}/not", f"{base_path}/pum.tar.gz"])
    assert "исходный путь не существует" in result

    result = tar([f"{base_path}/home/user", f"{base_path}/home/user/pum.tar.gz"])
    assert "запрещено архивировать папку в саму себя" in result
