TOPIC = "equality"

def test_string(file_path, get_command, run_program):
    path = file_path(TOPIC, "string")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "true\n"
    assert err == ""
    assert exit_code == 0

def test_numbers(file_path, get_command, run_program):
    path = file_path(TOPIC, "numbers")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "true\n"
    assert err == ""
    assert exit_code == 0

def test_mixed(file_path, get_command, run_program):
    path = file_path(TOPIC, "mixed")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "false\n"
    assert err == ""
    assert exit_code == 0

def test_grouped(file_path, get_command, run_program):
    path = file_path(TOPIC, "grouped")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "true\n"
    assert err == ""
    assert exit_code == 0