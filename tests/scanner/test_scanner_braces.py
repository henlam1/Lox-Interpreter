TOPIC = "braces"
        
def test_balanced(file_path, get_command, run_program):
    path = file_path(TOPIC, "balanced")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == '\n'.join([
        "LEFT_BRACE { null",
        "LEFT_BRACE { null",
        "RIGHT_BRACE } null",
        "LEFT_BRACE { null",
        "RIGHT_BRACE } null",
        "RIGHT_BRACE } null",
        "EOF  null\n"])
    assert err == ""
    assert exit_code == 0

def test_matched(file_path, get_command, run_program):
    path = file_path(TOPIC, "matched")
    command = get_command
    out, err, exit_code = run_program(command, path)
    
    assert out == '\n'.join([
        "LEFT_BRACE { null",
        "LEFT_BRACE { null",
        "RIGHT_BRACE } null",
        "RIGHT_BRACE } null",
        "EOF  null\n"
    ])
    assert err == ""
    assert exit_code == 0

def test_unbalanced(file_path, get_command, run_program):
    path = file_path(TOPIC, "unbalanced")
    command = get_command
    out, err, exit_code = run_program(command, path)
    
    assert out == '\n'.join([
        "LEFT_BRACE { null",
        "LEFT_BRACE { null",
        "RIGHT_BRACE } null",
        "LEFT_BRACE { null",
        "RIGHT_BRACE } null",
        "EOF  null\n"
    ])
    assert err == ""
    assert exit_code == 0

def test_unmatched(file_path, get_command, run_program):
    path = file_path(TOPIC, "unmatched")
    command = get_command
    out, err, exit_code = run_program(command, path)
    
    assert out == '\n'.join([
        "RIGHT_BRACE } null",
        "RIGHT_BRACE } null",
        "LEFT_BRACE { null",
        "LEFT_BRACE { null",
        "LEFT_BRACE { null",
        "EOF  null\n"
    ])
    assert err == ""
    assert exit_code == 0
