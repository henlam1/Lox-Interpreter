TOPIC = "literals"

def test_strings(file_path, get_command, run_program):
    path = file_path(TOPIC, "strings")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "hello\n"
    assert err == ""
    assert exit_code == 0

def test_integers(file_path, get_command, run_program):
    path = file_path(TOPIC, "integers")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "105\n"
    assert err == ""
    assert exit_code == 0

def test_decimals(file_path, get_command, run_program):
    path = file_path(TOPIC, "decimals")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "10.5\n"
    assert err == ""
    assert exit_code == 0
