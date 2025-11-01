import pytest
import sys


@pytest.fixture
def fs(fs):
    """Кроссплатформенная файловая система"""
    if sys.platform == "win32":
        base_path = "C:/"
    else:
        base_path = "/"

    fs.create_dir(f"{base_path}/home")
    fs.create_dir(f"{base_path}home/user")
    fs.create_file(f"{base_path}home/user/file1.txt")
    fs.create_dir(f"{base_path}home/user/subdir")
    fs.create_file(f"{base_path}home/user/subdir/file2.txt")
    fs.create_dir(f"{base_path}tmp")

    return fs

@pytest.fixture
def base_path():
    """Возвращает базовый путь для тестов"""
    if sys.platform == "win32":
        return "C:/"
    else:
        return "/"
