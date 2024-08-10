import pytest

COMMAND = "tokenize"
COMMAND_FOLDER = "scanning"

@pytest.fixture
def get_command():
    return COMMAND

@pytest.fixture
def make_command_path(base_path):
    return f"{base_path}/{COMMAND_FOLDER}"