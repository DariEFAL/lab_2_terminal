import shutil
from pathlib import Path


def untar(arguments: list, path_cwd: Path) -> str:
    """
    Реализация команды untar для распаковки архива .tar.gz
    :param argumentes: Список аргументов команды
    :return: "SUCCESS" при успешном выполнении или строку с ошибкой
    """

    if len(arguments) != 1:
        return "ERROR: неправильный синтаксис команды"

    arg_1 = Path(arguments[0]).expanduser().resolve()

    if arg_1.suffixes != [".tar", ".gz"]:
        return "ERROR: укажите архив с расширением .tar.gz"

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
