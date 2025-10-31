import os
from pathlib import Path

def cd(argumentes: list) -> str:
    """
    Реализация команды cd для изменения текущей рабочей директории
    :param argumentes: Список аргументов команды
    :return: "SUCCESS" при успешном выполнении или строку с ошибкой
    """

    if len(argumentes) != 1:
        return "ERROR: команда cd принимает ровно один аргумент"

    arg = Path(argumentes[0])

    if str(arg) == "~":
        arg = Path.home()

    try:
        os.chdir(arg)
    except Exception:
        return f"ERROR: {arg} не является директорией"

    return "SUCCESS"
