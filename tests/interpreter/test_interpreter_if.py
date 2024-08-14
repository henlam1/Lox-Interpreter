TOPIC = "if"

def test_if_else(file_path, get_command, run_program):
    path = file_path(TOPIC, "if_else")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "true\n"
    assert err == ""
    assert exit_code == 0

def test_if(file_path, get_command, run_program):
    path = file_path(TOPIC, "if")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "true\n"
    assert err == ""
    assert exit_code == 0

def test_missing_condition(file_path, get_command, run_program):
    path = file_path(TOPIC, "missing_condition")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == ""
    assert err == "".join([
        "[line 1] Error at {: Expect '(' after 'if'.\n",
        "[line 4] Error at }: Expect expression.\n"
        ])
    assert exit_code == 65