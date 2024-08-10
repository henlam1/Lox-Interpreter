import pytest
import subprocess
# from main import tokenize as _tokenize, parse as _parse, interpret as _interpret

# @pytest.fixture
# def tokenize() -> callable:
#     return _tokenize

# @pytest.fixture
# def parse() -> callable:
#     return _parse

# @pytest.fixture
# def interpret() -> callable:
#     return _interpret

BASE_PATH = "test_files/"

@pytest.fixture
def base_path():
    return BASE_PATH

@pytest.fixture
def file_path(make_command_path):
    def _file_path(topic, file_name):
        return f"{make_command_path}/{topic}/{file_name}.lox"
    
    return _file_path

@pytest.fixture
def make_full_command() -> callable:
    def _make_full_command(command, file_path):
        return f"python main.py {command} {file_path}"
    return _make_full_command

@pytest.fixture
def run_program(make_full_command) -> callable:
    def _run_program(command, file_path):
        full_command = make_full_command(command, file_path)
        result = subprocess.run(full_command, 
                                shell=True, 
                                capture_output=True,
                                text=True)
        
        # Normalize output and replace carriage returns
        output = result.stdout.replace('\r\n', '\n')
        errors = result.stderr.replace('\r\n', '\n')
        return output, errors, result.returncode
        
    return _run_program