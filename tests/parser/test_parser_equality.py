TOPIC = "equality"

def test_bang_equal(file_path, get_command, run_program):
    path = file_path(TOPIC, "bang_equal")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "(!= bar foo)\n"
    assert err == ""
    assert exit_code == 0

def test_equal_equal(file_path, get_command, run_program):
    path = file_path(TOPIC, "equal_equal")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "(== bar foo)\n"
    assert err == ""
    assert exit_code == 0

def test_numbers(file_path, get_command, run_program):
    path = file_path(TOPIC, "numbers")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "(== 67.0 41.0)\n"
    assert err == ""
    assert exit_code == 0

def test_nested(file_path, get_command, run_program):
    path = file_path(TOPIC, "nested")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "(== (group (!= 47.0 11.0)) (group (>= (group (+ (- 98.0) 16.0)) (group (* 31.0 91.0)))))\n"
    assert err == ""
    assert exit_code == 0