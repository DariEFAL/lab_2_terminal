from pathlib import Path


def cat(argumentes: list) -> str:
    """
    Реализация команды cat для вывода содержимого файлов
    :param argumentes: Список аргументов команды
    :return: "SUCCESS" при успешном выполнении или строку с ошибкой
    """

    if len(argumentes) != 1:
        return "ERROR: команда cat принимает ровно один аргумент"

    arg = Path(argumentes[0]).expanduser().resolve()

    try:
        print(arg.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return f"ERROR: файла {arg} не существует"
    except PermissionError:
        return f"ERROR: доступ к файлу {arg} запрещён"
    except OSError:
        return "ERROR: системная ошибка"
    except Exception:
        return f"ERROR: {arg} не является файлом"

    return "SUCCESS"
