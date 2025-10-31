import shutil
from pathlib import Path


def mv(argumentes: list) -> str:
    """
    Реализация команды mv для перемещения и переименования файлов и директорий
    :param argumentes: Список аргументов команды
    :return: "SUCCESS" при успешном выполнении или строку с ошибкой
    """

    if len(argumentes) != 2:
        return "ERROR: неправильный синтаксис команды"

    arg_1, arg_2 = [Path(i) for i in argumentes]

    try:
        if arg_1.is_dir():
            if arg_2.is_file():
                    return "ERROR: невозможно переместить директорию в файл"
            if arg_2.is_dir() and arg_1.resolve() in arg_2.resolve().parents:
                    return "ERROR: невозможно переместить директорию в саму себя"

        shutil.move(arg_1, arg_2)

        return "SUCCESS"
    except FileNotFoundError:
        return "ERROR: исходный файл или директория не существует"
    except PermissionError:
        return "ERROR: доступ запрещён"
    except NotADirectoryError:
        return f"ERROR: неверно задано имя директории: {arg_1}"
    except OSError:
         return "ERROR: Системная ошибка"
