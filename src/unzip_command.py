import shutil
from pathlib import Path


def unzip(arguments: list, path_cwd: Path) -> str:
    """
    Реализация команды unzip для распаковки архива .zip
    :param argumentes: Список аргументов команды
    :return: "SUCCESS" при успешном выполнении или строку с ошибкой
    """

    if len(arguments) != 1:
        return "ERROR: неправильный синтаксис команды"

    arg_1 = Path(arguments[0]).expanduser().resolve()

    if arg_1.suffix != ".zip":
        return "ERROR: укажите архив с расширением .zip"

    try:
        if arg_1.exists():
            shutil.unpack_archive(str(arg_1), str(path_cwd))

        else:
            return "ERROR: архив не существует"

        return "SUCCESS"
    except OSError:
        return "ERROR: Системная ошибка"
    except Exception as e:
        return f"ERROR: {e}"
