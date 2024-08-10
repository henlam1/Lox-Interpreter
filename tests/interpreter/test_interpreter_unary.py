TOPIC = "unary"

def test_negation(file_path, get_command, run_program):
    path = file_path(TOPIC, "negation")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "-83\n"
    assert err == ""
    assert exit_code == 0

def test_nested_not(file_path, get_command, run_program):
    path = file_path(TOPIC, "nested_not")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "false\n"
    assert err == ""
    assert exit_code == 0

def test_nil(file_path, get_command, run_program):
    path = file_path(TOPIC, "nil")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "true\n"
    assert err == ""
    assert exit_code == 0

def test_not(file_path, get_command, run_program):
    path = file_path(TOPIC, "not")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "false\n"
    assert err == ""
    assert exit_code == 0

def test_numbers(file_path, get_command, run_program):
    path = file_path(TOPIC, "numbers")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "true\n"
    assert err == ""
    assert exit_code == 0