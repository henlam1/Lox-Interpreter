TOPIC = "parenthesis"

def test_balanced(file_path, get_command, run_program):
    path = file_path(TOPIC, "balanced")
    command = get_command
    out, err, exit_code = run_program(command, path)
    out == '\n'.join([
        "LEFT_PAREN ( null",
        "LEFT_PAREN ( null",
        "RIGHT_PAREN ) null",
        "LEFT_PAREN ( null",
        "RIGHT_PAREN ) null",
        "RIGHT_PAREN ) null",
        "EOF  null\n"
    ])
    assert err == ""
    assert exit_code == 0

def test_matched(file_path, get_command, run_program):
    path = file_path(TOPIC, "matched")
    command = get_command
    out, err, exit_code = run_program(command, path)
    out == '\n'.join([
        "LEFT_PAREN ( null",
        "LEFT_PAREN ( null",
        "RIGHT_PAREN ) null",
        "RIGHT_PAREN ) null",
        "EOF  null\n"
    ])
    assert err == ""
    assert exit_code == 0

def test_unbalanced(file_path, get_command, run_program):
    path = file_path(TOPIC, "unbalanced")
    command = get_command
    out, err, exit_code = run_program(command, path)
    out == '\n'.join([
        "LEFT_PAREN ( null",
        "LEFT_PAREN ( null",
        "RIGHT_PAREN ) null",
        "LEFT_PAREN ( null",
        "RIGHT_PAREN ) null",
        "EOF  null\n"
    ])
    assert err == ""
    assert exit_code == 0

def test_unmatched(file_path, get_command, run_program):
    path = file_path(TOPIC, "unmatched")
    command = get_command
    out, err, exit_code = run_program(command, path)
    out == '\n'.join([
        "RIGHT_PAREN ) null",
        "RIGHT_PAREN ) null",
        "LEFT_PAREN ( null",
        "LEFT_PAREN ( null",
        "LEFT_PAREN ( null",
        "EOF  null\n"
    ])
    assert err == ""
    assert exit_code == 0
