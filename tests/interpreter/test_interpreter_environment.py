TOPIC = "environment"

def test_nesting(file_path, get_command, run_program):
    path = file_path(TOPIC, "nesting")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "".join([
        "inner a\n",
        "outer b\n",
        "global c\n",
        "outer a\n",
        "outer b\n",
        "global c\n",
        "global a\n",
        "global b\n",
        "global c\n",
    ])
    assert err == ""
    assert exit_code == 0

def test_shadowing(file_path, get_command, run_program):
    path = file_path(TOPIC, "shadowing")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == "apple\nworld\n"
    assert err == ""
    assert exit_code == 0

def test_undefined_var(file_path, get_command, run_program):
    path = file_path(TOPIC, "undefined_var")
    command = get_command
    out, err, exit_code = run_program(command, path)
    assert out == ""
    assert err == "Undefined variable 'x'.\n[line 2]\n"
    assert exit_code == 70