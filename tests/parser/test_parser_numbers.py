TOPIC = "numbers"

def test_integer(file_path, get_command, run_program):
    path = file_path(TOPIC, "integer")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "1.0\n"
    assert err == ""
    assert exit_code == 0

def test_decimal(file_path, get_command, run_program):
    path = file_path(TOPIC, "decimal")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "32.32\n"
    assert err == ""
    assert exit_code == 0

def test_zero(file_path, get_command, run_program):
    path = file_path(TOPIC, "zero")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "0.0\n"
    assert err == ""
    assert exit_code == 0