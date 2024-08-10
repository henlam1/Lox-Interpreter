TOPIC = "numbers"

def test_decimals(file_path, get_command, run_program):
    path = file_path(TOPIC, "decimals")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == '\n'.join([
        "NUMBER 123.456 123.456",
        "DOT . null",
        "NUMBER 456 456.0",
        "NUMBER 123 123.0",
        "DOT . null",
        "EOF  null\n"])
    assert err == ""
    assert exit_code == 0

def test_integers(file_path, get_command, run_program):
    path = file_path(TOPIC, "integers")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == '\n'.join([
        "NUMBER 123 123.0",
        "NUMBER 456 456.0",
        "EOF  null\n"])
    assert err == ""
    assert exit_code == 0