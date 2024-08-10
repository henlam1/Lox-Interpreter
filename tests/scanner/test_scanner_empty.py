TOPIC = "empty"

def test_empty(file_path, get_command, run_program):
    path = file_path(TOPIC, "empty_file")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "EOF  null\n"
    assert err == ""
    assert exit_code == 0