TOPIC = "comparison"

def test_less(file_path, get_command, run_program):
    path = file_path(TOPIC, "less")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "(< (< 70.0 95.0) 120.0)\n"
    assert err == ""
    assert exit_code == 0

def test_less_equals(file_path, get_command, run_program):
    path = file_path(TOPIC, "less_equals")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "(<= 25.0 95.0)\n"
    assert err == ""
    assert exit_code == 0

def test_greater(file_path, get_command, run_program):
    path = file_path(TOPIC, "greater")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "(> 70.0 45.0)\n"
    assert err == ""
    assert exit_code == 0

def test_greater_equals(file_path, get_command, run_program):
    path = file_path(TOPIC, "greater_equals")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "(>= (group (- 58.0 40.0)) (- (group (+ (/ 82.0 19.0) 16.0))))\n"
    assert err == ""
    assert exit_code == 0