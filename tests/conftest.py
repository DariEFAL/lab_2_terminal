import pytest
import sys


@pytest.fixture
def fs(fs):
    """
    фейковая файловая система
    """

    if sys.platform == "win32":
        base_path = "C:/"
    else:
        base_path = "/"

    fs.create_dir(f"{base_path}/home")
    fs.create_dir(f"{base_path}/home/user")
    fs.create_file(f"{base_path}/home/user/laba.txt", contents="лаба по питону", encoding="utf-8")
    fs.create_dir(f"{base_path}/home/user/project")
    fs.create_file(f"{base_path}/home/user/project/infa.py", contents="print(1)", encoding="utf-8")
    fs.create_dir(f"{base_path}/tmp")
    fs.create_file(f"{base_path}/import.txt", contents="очень важно", encoding="utf-8")

    return fs

@pytest.fixture
def base_path():
    """
    Возвращает базовый путь для тестов
    """

    if sys.platform == "win32":
        return "C:/"
    else:
        return "/"
