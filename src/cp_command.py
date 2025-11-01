import shutil
import os
from pathlib import Path


def cp(arguments: list) -> str:
    """
    Реализация команды cp для копирования файлов и директорий
    :param argumentes: Список аргументов команды
    :return: "SUCCESS" при успешном выполнении или строку с ошибкой
    """

    if len(arguments) - arguments.count("-r") != 2:
        return "ERROR: неправильный синтаксис команды"

    arg_1, arg_2 = [Path(i).expanduser().resolve() for i in arguments if i != "-r"]

    try:
        if "-r" in arguments:
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
        return "ERROR: неправильный путь"
    except PermissionError:
        return "ERROR: доступ запрещён"
    except OSError:
         return "ERROR: Системная ошибка"
