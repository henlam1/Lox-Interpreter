TOPIC = "logical"

def test_and(file_path, get_command, run_program):
    path = file_path(TOPIC, "and")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "false\n4\n"
    assert err == ""
    assert exit_code == 0

def test_or(file_path, get_command, run_program):
    path = file_path(TOPIC, "or")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "hi\nyes\n"
    assert err == ""
    assert exit_code == 0