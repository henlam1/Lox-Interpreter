TOPIC = "identifiers"

def test_one_identifier(file_path, get_command, run_program):
    path = file_path(TOPIC, "one_identifier")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == '\n'.join([
        "IDENTIFIER hello null",
        "EOF  null\n"])
    assert err == ""
    assert exit_code == 0

def test_many_identifiers(file_path, get_command, run_program):
    path = file_path(TOPIC, "many_identifiers")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == '\n'.join([
        "IDENTIFIER foo null",
        "NUMBER 5.6 5.6",
        "IDENTIFIER _hello null",
        "EOF  null\n"])
    assert err == ""
    assert exit_code == 0