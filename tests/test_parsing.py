from src.parsing import command_parsing


def test_command_parsing_basic():
    """Проверка парсинга"""

    result = command_parsing("cp a.py b.py")
    assert result == ["cp", "a.py", "b.py"]

    result = command_parsing("ls")
    assert result == ["ls"]

    result = command_parsing("rm -r d")
    assert result == ["rm", "-r", "d"]

    result = command_parsing("cp   a         b")
    assert result == ["cp", "a", "b"]

    result = command_parsing('cp "f f f.txt" f')
    assert result == ["cp", "f f f.txt", "f"]

    result = command_parsing("cp 'f f f.txt' f")
    assert result == ["cp", "f f f.txt", "f"]

    result = command_parsing("cp 'f \"f\" f.txt' f")
    assert result == ["cp", "f \"f\" f.txt", "f"]

    result = command_parsing("cp \'f \"\'f\" \'f\".txt f")
    assert result == ["cp", "f \"f \'f.txt", "f"]

    result = command_parsing("cp 'f f f.txt f")
    assert result == "ERROR: пропущена закрывающая кавычка"

    result = command_parsing("")
    assert result == []

    result = command_parsing("   ")
    assert result == []

    result = command_parsing("   ' '")
    assert result == []
