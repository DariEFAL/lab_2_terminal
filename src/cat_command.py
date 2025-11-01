from pathlib import Path


def cat(arguments: list) -> str:
    """
    Реализация команды cat для вывода содержимого файлов
    :param argumentes: Список аргументов команды
    :return: "SUCCESS" при успешном выполнении или строку с ошибкой
    """

    if len(arguments) != 1:
        return "ERROR: команда cat принимает ровно один аргумент"

    arg = Path(arguments[0]).expanduser().resolve()

    if arg.exists() and not arg.is_file():
        return f"ERROR: {arg} не является файлом"
    if not arg.exists():
        return f"ERROR: файла {arg} не существует"

    try:
        print(arg.read_text(encoding="utf-8"))
    except PermissionError:
        return f"ERROR: доступ к файлу/директорию {arg} запрещён"
    except Exception as e:
        return f"ERROR: {e}"

    return "SUCCESS"
