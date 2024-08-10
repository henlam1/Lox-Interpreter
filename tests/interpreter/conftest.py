import pytest

COMMAND = "evaluate"
COMMAND_FOLDER = "interpreting"
    
@pytest.fixture
def get_command():
    return COMMAND

@pytest.fixture
def make_command_path(base_path):
    return f"{base_path}/{COMMAND_FOLDER}"


# def test_(file_path, get_command, run_program):
#     path = file_path(TOPIC, "")
#     command = get_command
#     out, err, exit_code = run_program(command, path)
#     assert out == "\n"
#     assert err == ""
#     assert exit_code == 0