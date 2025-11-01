import os
from pathlib import Path

def cd(arguments: list) -> str:
    """
    Реализация команды cd для изменения текущей рабочей директории
    :param argumentes: Список аргументов команды
    :return: "SUCCESS" при успешном выполнении или строку с ошибкой
    """

    if len(arguments) != 1:
        return "ERROR: команда cd принимает ровно один аргумент"

    arg = Path(arguments[0]).expanduser().resolve()

    try:
        os.chdir(arg)
    except FileNotFoundError:
        return f"ERROR: директория {arg} не существует"
    except NotADirectoryError:
        return "ERROR: {arg} не является директорией"
    except PermissionError:
        return f"ERROR: доступ к директории {arg} запрещён"
    except OSError:
        return "ERROR: системная ошибка"
    except Exception:
        return f"ERROR: не удалось перейти в директорию {arg}"

    return "SUCCESS"
