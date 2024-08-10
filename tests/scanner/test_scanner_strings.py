TOPIC = "strings"

def test_empty_string(file_path, get_command, run_program):
    path = file_path(TOPIC, "empty_string")
    command = get_command
    out, err, exit_code = run_program(command, path)
    out == '\n'.join([
        "STRING \"\" ",
        "EOF  null\n"])
    assert err == ""
    assert exit_code == 0

def test_integers(file_path, get_command, run_program):
    path = file_path(TOPIC, "regular")
    command = get_command
    out, err, exit_code = run_program(command, path)
    out == '\n'.join([
        "STRING \"foo      bar 123 // hello world!\" foo      bar 123 // hello world!",
        "EOF  null\n"])
    assert err == ""
    assert exit_code == 0