TOPIC = "unary"

def test_bang(file_path, get_command, run_program):
    path = file_path(TOPIC, "bang")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "(! true)\n"
    assert err == ""
    assert exit_code == 0

def test_minus(file_path, get_command, run_program):
    path = file_path(TOPIC, "minus")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "(- 81.9)\n"
    assert err == ""
    assert exit_code == 0

def test_nested(file_path, get_command, run_program):
    path = file_path(TOPIC, "nested")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "(! (group (! (group true))))\n"
    assert err == ""
    assert exit_code == 0
