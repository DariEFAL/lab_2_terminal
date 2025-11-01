import shutil
import os
from pathlib import Path


def cp(argumentes: list) -> str:
    """
    Реализация команды cp для копирования файлов и директорий
    :param argumentes: Список аргументов команды
    :return: "SUCCESS" при успешном выполнении или строку с ошибкой
    """

    if len(argumentes) - argumentes.count("-r") != 2:
        return "ERROR: неправильный синтаксис команды"

    arg_1, arg_2 = [Path(i).expanduser().resolve() for i in argumentes if i != "-r"]

    try:
        if "-r" in argumentes:
            if arg_2.is_file():
                return "ERROR: невозможно скопировать директорию в файл"
            if arg_2.exists():
                arg_2 = Path(os.path.join(arg_2, arg_1.name))
            if arg_1 in arg_2.parents:
                return "ERROR: невозможно скопировать директорию в саму себя"
            shutil.copytree(arg_1, arg_2)

        else:
            if arg_1.is_dir():
                return "ERROR: для копирования директории используйте флаг -r"
            shutil.copy2(arg_1, arg_2)

        return "SUCCESS"
    except FileNotFoundError:
        return "ERROR: исходный файл или директория не существует"
    except PermissionError:
        return "ERROR: доступ запрещён"
    except NotADirectoryError:
        return f"ERROR: неверно задано имя директории: {arg_1}"
    except OSError:
         return "ERROR: Системная ошибка"
