from pathlib import Path
import stat
import datetime


def ls_detailed(path: Path) -> None:
    """
    Выводит подробную информацию о содержимом директории/файла
    :param path: Путь к директории для вывода информации
    :return: None
    """

    path_stat = path.stat()
    mode = path_stat.st_mode

    print(f"{stat.filemode(mode)} {path_stat.st_size:10} {datetime.datetime.fromtimestamp(path_stat.st_mtime).strftime("%b %d %H:%M"):12} {path.name}")

def ls(argumentes: list, path_cwd: Path) -> str:
    """
    Реализация команды ls для вывода содержимого директории
    :param argumentes: Список аргументов команды
    :param path_cwd: Путь к текущей рабочей директории
    :return: "SUCCESS" при успешном выполнении или строку с ошибкой
    """

    flag_l = False

    if "-l" in argumentes:
        flag_l = True
    if not argumentes or argumentes.count("-l") == len(argumentes):
        argumentes.append(path_cwd)

    for arg in argumentes:
        if arg == "-l":
            continue

        arg = Path(arg).expanduser().resolve()

        if arg.is_file():
            print("Каталог:", arg.parent)
            if flag_l:
                ls_detailed(arg)
            else:
                print(arg.name)

        elif arg.is_dir():
            print("Каталог:", arg)
            if flag_l:
                for child in sorted(arg.iterdir()):
                    ls_detailed(child)
            else:
                for child in sorted(arg.iterdir()):
                    print(child.name, end="  ")
                print()

        else:
            return f"ERROR: путь {arg} не существует"

    return "SUCCESS"
