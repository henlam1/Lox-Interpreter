TOPIC = "arithmetic"

def test_mul_div(file_path, get_command, run_program):
    path = file_path(TOPIC, "mul_div")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "(/ (* 45.0 88.0) 33.0)\n"
    assert err == ""
    assert exit_code == 0

def test_pemdas(file_path, get_command, run_program):
    path = file_path(TOPIC, "pemdas")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "(/ (* (- (group (+ (- 96.0) 25.0))) (group (* 58.0 51.0))) (group (+ 71.0 63.0)))\n"
    assert err == ""
    assert exit_code == 0

def test_string_concat(file_path, get_command, run_program):
    path = file_path(TOPIC, "string_concat")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "(+ hello world)\n"
    assert err == ""
    assert exit_code == 0
