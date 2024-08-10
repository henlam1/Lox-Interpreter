TOPIC = "errors"

def test_missing_parenthesis(file_path, get_command, run_program):
    path = file_path(TOPIC, "missing_parenthesis")
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

def test_missing_primary(file_path, get_command, run_program):
    path = file_path(TOPIC, "missing_primary")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == ""
    assert err == "[line 1] Error at end: Expect expression.\n"
    assert exit_code == 65