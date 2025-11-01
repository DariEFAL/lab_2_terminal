import shutil
from pathlib import Path


def zip(arguments: list) -> str:
    """
    Реализация команды zip для архивирования файлов и директорий
    :param argumentes: Список аргументов команды
    :return: "SUCCESS" при успешном выполнении или строку с ошибкой
    """

    if len(arguments) != 2:
        return "ERROR: неправильный синтаксис команды"

    arg_1, arg_2 = [Path(i).expanduser().resolve() for i in arguments]

    if arg_2.suffix != ".zip":
        return f"ERROR: укажите расширение .zip для {arg_2}"
    if arg_2.is_relative_to(arg_1):
        return "ERROR: запрещено архивировать папку в саму себя"

    try:
        if arg_1.is_file():
            shutil.make_archive(base_name=str(arg_2.with_suffix('')),
                                format="zip",
                                root_dir=arg_1.parent,
                                base_dir=arg_1.name)
        elif arg_1.is_dir():
            shutil.make_archive(base_name=str(arg_2.with_suffix('')),
                                format="zip",
                                root_dir=arg_1)
        else:
            return "ERROR: исходный путь не существует"

        return "SUCCESS"
    except OSError:
        return "ERROR: Системная ошибка"
    except Exception as e:
        return f"ERROR: {e}"
