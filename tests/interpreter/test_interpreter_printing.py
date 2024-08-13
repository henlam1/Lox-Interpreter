TOPIC = "printing"

def test_bools(file_path, get_command, run_program):
    path = file_path(TOPIC, "bools")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "false\n"
    assert err == ""
    assert exit_code == 0

def test_exprs(file_path, get_command, run_program):
    path = file_path(TOPIC, "exprs")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "2\n"
    assert err == ""
    assert exit_code == 0

def test_strings(file_path, get_command, run_program):
    path = file_path(TOPIC, "strings")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "hello world\n"
    assert err == ""
    assert exit_code == 0