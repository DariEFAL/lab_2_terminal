from src.unzip_command import unzip
from pathlib import Path


def test_unzip(fs, base_path):
    """
    Проверяет работу функции unzip
    """

    result = unzip([], Path(f"{base_path}"))
    assert "неправильный синтаксис команды" in result

    result = unzip([f"{base_path}/test.zip", "extra"], Path(f"{base_path}"))
    assert "неправильный синтаксис команды" in result

    result = unzip([f"{base_path}/test.tar.gz"], Path(f"{base_path}"))
    assert "укажите архив с расширением .zip" in result

    result = unzip([f"{base_path}/test.txt"], Path(f"{base_path}"))
    assert "укажите архив с расширением .zip" in result

    result = unzip([f"{base_path}/not.zip"], Path(f"{base_path}"))
    assert "архив не существует" in result
