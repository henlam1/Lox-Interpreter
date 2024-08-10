TOPIC = "arithmetic"

def test_multiply(file_path, get_command, run_program):
    path = file_path(TOPIC, "multiply")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "1275\n"
    assert err == ""
    assert exit_code == 0

def test_divide(file_path, get_command, run_program):
    path = file_path(TOPIC, "divide")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "8.2\n"
    assert err == ""
    assert exit_code == 0

def test_minus(file_path, get_command, run_program):
    path = file_path(TOPIC, "minus")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "-25\n"
    assert err == ""
    assert exit_code == 0

def test_add(file_path, get_command, run_program):
    path = file_path(TOPIC, "add")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "6\n"
    assert err == ""
    assert exit_code == 0

def test_pemdas(file_path, get_command, run_program):
    path = file_path(TOPIC, "pemdas")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "-8613\n"
    assert err == ""
    assert exit_code == 0