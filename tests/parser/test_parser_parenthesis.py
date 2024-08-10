TOPIC = "parenthesis"

def test_incomplete(file_path, get_command, run_program):
    path = file_path(TOPIC, "incomplete")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == ""
    assert err == "[line 1] Error at end: Expect ')' after expression.\n"
    assert exit_code == 65

def test_missing_expr(file_path, get_command, run_program):
    path = file_path(TOPIC, "missing_expr")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == ""
    assert err == "[line 1] Error at ): Expect expression.\n"
    assert exit_code == 65

def test_nested(file_path, get_command, run_program):
    path = file_path(TOPIC, "nested")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "(group (group true))\n"
    assert err == ""
    assert exit_code == 0

def test_single(file_path, get_command, run_program):
    path = file_path(TOPIC, "single")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "(group foo)\n"
    assert err == ""
    assert exit_code == 0


