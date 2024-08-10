TOPIC = "reserved"

def test_reserved(file_path, get_command, run_program):
    path = file_path(TOPIC, "reserved")
    command = get_command
    out, err, exit_code = run_program(command, path)
    out == '\n'.join([
        "AND and null",
        "CLASS class null",
        "ELSE else null",
        "FALSE false null", 
        "FOR for null",
        "FUN fun null",
        "IF if null",
        "NIL nil null",
        "OR or null",
        "PRINT print null",
        "RETURN return null",
        "SUPER super null",
        "THIS this null",
        "TRUE true null",
        "VAR var null",
        "WHILE while null",
        "EOF  null\n"])
    assert err == ""
    assert exit_code == 0

def test_statements(file_path, get_command, run_program):
    path = file_path(TOPIC, "statements")
    command = get_command
    out, err, exit_code = run_program(command, path)
    out == '\n'.join([
        "VAR var null",
        "IDENTIFIER greeting null",
        "EQUAL = null",
        "STRING \"Hello\" Hello",
        "IF if null",
        "LEFT_PAREN ( null",
        "IDENTIFIER greeting null",
        "EQUAL_EQUAL == null",
        "STRING \"Hello\" Hello",
        "RIGHT_PAREN ) null",
        "LEFT_BRACE { null",
        "RETURN return null",
        "TRUE true null",
        "RIGHT_BRACE } null",
        "ELSE else null",
        "LEFT_BRACE { null",
        "RETURN return null",
        "FALSE false null",
        "RIGHT_BRACE } null",
        "EOF  null\n"])
    assert err == ""
    assert exit_code == 0