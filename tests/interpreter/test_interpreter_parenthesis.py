TOPIC = "parenthesis"

def test_nested(file_path, get_command, run_program):
    path = file_path(TOPIC, "nested")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "false\n"
    assert err == ""
    assert exit_code == 0

def test_strings(file_path, get_command, run_program):
    path = file_path(TOPIC, "strings")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "hello\n"
    assert err == ""
    assert exit_code == 0

def test_numbers(file_path, get_command, run_program):
    path = file_path(TOPIC, "numbers")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "10.5\n"
    assert err == ""
    assert exit_code == 0