TOPIC = "errors"

def test_invalid_chars(file_path, get_command, run_program):
    path = file_path(TOPIC, "invalid_chars")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == '\n'.join([
        "LEFT_BRACE { null",
        "LEFT_PAREN ( null",
        "DOT . null",
        "MINUS - null",
        "COMMA , null",
        "RIGHT_PAREN ) null",
        "RIGHT_BRACE } null",
        "EOF  null\n"])
    assert err == '\n'.join([
        "[line 1] Error: Unexpected character: %",
        "[line 1] Error: Unexpected character: $\n"])
    assert exit_code == 65

def test_multiline_invalid_chars(file_path, get_command, run_program):
    path = file_path(TOPIC, "multiline_invalid_chars")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == '\n'.join([
        "LEFT_PAREN ( null",
        "RIGHT_PAREN ) null",
        "EOF  null\n"])
    assert err == '\n'.join([
        "[line 1] Error: Unexpected character: #",
        "[line 2] Error: Unexpected character: @\n"])
    assert exit_code == 65

def test_unterminated_string(file_path, get_command, run_program):
    path = file_path(TOPIC, "unterminated_string")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "EOF  null\n"
    assert err == "[line 1] Error: Unterminated string.\n"
    assert exit_code == 65