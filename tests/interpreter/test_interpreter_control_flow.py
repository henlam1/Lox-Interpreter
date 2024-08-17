TOPIC = "control_flow"

def test_while(file_path, get_command, run_program):
    path = file_path(TOPIC, "while")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "0\n1\n2\n"
    assert err == ""
    assert exit_code == 0

def test_for(file_path, get_command, run_program):
    path = file_path(TOPIC, "for")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "0\n1\n2\n"
    assert err == ""
    assert exit_code == 0