TOPIC = "booleans"

def test_true(file_path, get_command, run_program):
    path = file_path(TOPIC, "true")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "true\n"
    assert err == ""
    assert exit_code == 0

def test_false(file_path, get_command, run_program):
    path = file_path(TOPIC, "false")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "false\n"
    assert err == ""
    assert exit_code == 0

def test_nil(file_path, get_command, run_program):
    path = file_path(TOPIC, "nil")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "nil\n"
    assert err == ""
    assert exit_code == 0