def command_parsing(command_str: str) -> list[str] | str:
    """
    Парсит строку команды на составляющие
    :param command_str: Строка команды
    :return: Список аргументов или строку с ошибкой
    """

    quote = ""
    command = []
    token = ""

    for i in command_str:
        if i == ' ':
            if not quote and token:
                command.append(token)
                token = ""
                continue
            elif not token:
                continue

        elif i == "'" or i == '"':
            if not quote:
                quote = i
                continue
            elif i == quote:
                quote = ""
                continue

        token += i

    if quote:
        return "ERROR: пропущена закрывающая кавычка"

    if token:
        command.append(token)

    return command
