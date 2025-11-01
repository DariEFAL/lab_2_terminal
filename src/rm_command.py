import shutil
from pathlib import Path


def rm(arguments: list, path_cwd: Path) -> str:
    """
    Реализация команды rm для удаления файлов и директорий
    :param argumentes: Список аргументов команды
    :param path_cwd: Путь к текущей рабочей директории
    :return: "SUCCESS" при успешном выполнении или строку с ошибкой
    """

    if len(arguments) - arguments.count("-r") != 1:
        return "ERROR: неправильный синтаксис команды"

    arg = [Path(i).expanduser().resolve() for i in arguments if i != "-r"][0]

    try:
        if arg.is_file():
            arg.unlink()

        elif arg.is_dir():
            if "-r" not in arguments:
                return "ERROR: для удаления директории используйте флаг -r"
            if arg == Path("C:/") or arg == Path("/"):
                return "ERROR: запрещено удалять корневой каталог"
            if arg.resolve() in path_cwd.parents or arg.resolve() == path_cwd:
                return "ERROR: запрещено удалять текущую или родительскую директорию"
            if input(f"Удалить каталог '{arg.resolve()}'? (y/n): ") == "y":
                shutil.rmtree(arg)
            else:
                return "CANCELLED: удаление отменено пользователем"

        else:
            return f"ERROR: {arg} не является файлом или директорией"

        return "SUCCESS"
    except PermissionError:
        return "ERROR: доступ запрещён"
    except OSError:
         return "ERROR: Системная ошибка"
