TOPIC = "runtime_errors"

def test_unary_string(file_path, get_command, run_program):
    path = file_path(TOPIC, "unary_string")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == ""
    assert err == "Operand must be a number.\n[line 1]\n"
    assert exit_code == 70

def test_unary_bool(file_path, get_command, run_program):
    path = file_path(TOPIC, "unary_bool")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == ""
    assert err == "Operand must be a number.\n[line 1]\n"
    assert exit_code == 70

def test_unary_group(file_path, get_command, run_program):
    path = file_path(TOPIC, "unary_group")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == ""
    assert err == "Operand must be a number.\n[line 1]\n"
    assert exit_code == 70

def test_invalid_mul_operands(file_path, get_command, run_program):
    path = file_path(TOPIC, "invalid_mul_operands")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == ""
    assert err == "Operands must be numbers.\n[line 1]\n"
    assert exit_code == 70

def test_invalid_div_operands(file_path, get_command, run_program):
    path = file_path(TOPIC, "invalid_div_operands")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == ""
    assert err == "Operands must be numbers.\n[line 1]\n"
    assert exit_code == 70

def test_invalid_plus_operands(file_path, get_command, run_program):
    path = file_path(TOPIC, "invalid_plus_operands")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == ""
    assert err == "Operands must be numbers or strings\n[line 1]\n"
    assert exit_code == 70

def test_invalid_minus_operands(file_path, get_command, run_program):
    path = file_path(TOPIC, "invalid_minus_operands")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == ""
    assert err == "Operands must be numbers.\n[line 1]\n"
    assert exit_code == 70

def test_invalid_less_operands(file_path, get_command, run_program):
    path = file_path(TOPIC, "invalid_less_operands")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == ""
    assert err == "Operands must be numbers.\n[line 1]\n"
    assert exit_code == 70

def test_invalid_less_equals_operands(file_path, get_command, run_program):
    path = file_path(TOPIC, "invalid_less_equals_operands")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == ""
    assert err == "Operands must be numbers.\n[line 1]\n"
    assert exit_code == 70

def test_invalid_greater_operands(file_path, get_command, run_program):
    path = file_path(TOPIC, "invalid_greater_operands")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == ""
    assert err == "Operands must be numbers.\n[line 1]\n"
    assert exit_code == 70

def test_invalid_greater_equals_operands(file_path, get_command, run_program):
    path = file_path(TOPIC, "invalid_greater_equals_operands")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == ""
    assert err == "Operands must be numbers.\n[line 1]\n"
    assert exit_code == 70

# def test_(file_path, get_command, run_program):
#     path = file_path(TOPIC, "")
#     command = get_command
#     out, err, exit_code = run_program(command, path)
#     assert out == "\n"
#     assert err == ""
#     assert exit_code == 0