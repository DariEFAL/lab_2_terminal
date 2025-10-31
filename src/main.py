from src.terminal import Terminal


def main() -> None:
    """
    Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """

    user = Terminal()
    user.run()

if __name__ == "__main__":
    main()
