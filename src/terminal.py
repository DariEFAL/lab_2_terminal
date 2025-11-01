from pathlib import Path
import logging

from src.parsing import command_parsing
from src.ls_command import ls
from src.cd_command import cd
from src.cat_command import cat
from src.cp_command import cp
from src.mv_command import mv
from src.rm_command import rm


class Terminal:
    """
    Запуск терминала и обработка команд
    :param: Ничего не принимает
    :return: Ничего не возвращает
    """

    def __init__(self) -> None:
        self.path_cwd = Path.cwd()
        self._logging()

    def _logging(self) -> None:
        """Настраивает логирование"""
        logging.basicConfig(level=logging.INFO,
                            filename="shell.log",
                            format="[%(asctime)s] %(message)s",
                            datefmt="%Y-%m-%d %H:%M:%S",
                            encoding="utf-8")

        self.logger = logging.getLogger("terminal")

    def success_or_error(self, result: str) -> bool:
        """Обрабатывает результат выполнения команды и записывает в shell.log"""
        if result == "SUCCESS":
            self.logger.info(result)
            return True

        else:
            self.logger.error(result)
            print(result)
            return False

    def run(self) -> None:
        "Запускает основной цикл терминала"
        while True:
            command_str = input(f"{self.path_cwd}> ")
            self.logger.info(command_str)
            command = command_parsing(command_str)

            if isinstance(command, str):
                self.success_or_error(command)
                continue
            if not command:
                continue
            if command[0] == "exit":
                self.success_or_error("SUCCESS")
                return None

            match command[0]:
                case 'ls':
                    result = ls(command[1:], self.path_cwd)
                    self.success_or_error(result)
                    continue

                case 'cd':
                    result = cd(command[1:])
                    if self.success_or_error(result):
                        self.path_cwd = Path.cwd()
                    continue

                case 'cat':
                    result = cat(command[1:])
                    self.success_or_error(result)
                    continue

                case 'cp':
                    result = cp(command[1:])
                    self.success_or_error(result)
                    continue

                case 'mv':
                    result = mv(command[1:])
                    self.success_or_error(result)
                    continue

                case 'rm':
                    result = rm(command[1:], self.path_cwd)
                    self.success_or_error(result)
                    continue

                case _:
                    result = f"ERROR: команда {command[0]} не найдена"
                    self.success_or_error(result)
