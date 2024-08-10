TOPIC = "string_concat"

def test_concat_two(file_path, get_command, run_program):
    path = file_path(TOPIC, "concat_two")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "fooquz\n"
    assert err == ""
    assert exit_code == 0

def test_concat_grouped(file_path, get_command, run_program):
    path = file_path(TOPIC, "concat_grouped")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "hellobarbarquz\n"
    assert err == ""
    assert exit_code == 0