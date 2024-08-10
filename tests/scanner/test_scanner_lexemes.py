TOPIC = "lexemes"

def test_single_tokens(file_path, get_command, run_program):
    path = file_path(TOPIC, "single_tokens")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == '\n'.join([
        "SEMICOLON ; null",
        "COMMA , null",
        "PLUS + null",
        "MINUS - null",
        "STAR * null",
        "SLASH / null",
        "LESS < null",
        "GREATER > null",
        "DOT . null",
        "EOF  null\n"])
    assert err == ""
    assert exit_code == 0

def test_double_tokens(file_path, get_command, run_program):
    path = file_path(TOPIC, "double_tokens")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == '\n'.join([
        "BANG_EQUAL != null",
        "EQUAL_EQUAL == null",
        "LESS_EQUAL <= null",
        "GREATER_EQUAL >= null",
        "BANG_EQUAL != null",
        "EOF  null\n"])
    assert err == ""
    assert exit_code == 0

def test_comments(file_path, get_command, run_program):
    path = file_path(TOPIC, "comments")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == '\n'.join([
        "LEFT_PAREN ( null",
        "EOF  null\n"])
    assert err == ""
    assert exit_code == 0