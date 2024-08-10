TOPIC = "strings"

def test_words(file_path, get_command, run_program):
    path = file_path(TOPIC, "words")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "hello quz\n"
    assert err == ""
    assert exit_code == 0

def test_numbers(file_path, get_command, run_program):
    path = file_path(TOPIC, "numbers")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "92\n"
    assert err == ""
    assert exit_code == 0

def test_lexemes(file_path, get_command, run_program):
    path = file_path(TOPIC, "lexemes")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "+=/* //hello\n"
    assert err == ""
    assert exit_code == 0
