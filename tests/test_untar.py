from src.untar_command import untar
from pathlib import Path


def test_untar(fs, base_path):
    """
    Проверяет работу функции untar
    """

    result = untar([], Path(f"{base_path}"))
    assert "неправильный синтаксис команды" in result

    result = untar([f"{base_path}/test.tar.gz", "extra"], Path(f"{base_path}"))
    assert "неправильный синтаксис команды" in result

    result = untar([f"{base_path}/test.zip"], Path(f"{base_path}"))
    assert "укажите архив с расширением .tar.gz" in result

    result = untar([f"{base_path}/test.txt"], Path(f"{base_path}"))
    assert "укажите архив с расширением .tar.gz" in result

    result = untar([f"{base_path}/not.tar.gz"], Path(f"{base_path}"))
    assert "архив не существует" in result
