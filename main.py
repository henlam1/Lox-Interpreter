import sys
from lox.lox import Lox
from lox.scanner import Scanner
from lox.parser import Parser
from lox.interpreter import Interpreter

def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py tokenize/parse/evaluate <filename>", file=sys.stderr)
        exit(1)

    command = sys.argv[1]
    filename = sys.argv[2]

    with open(filename) as file:
        file_contents = file.read()
    
    match command:
        case "tokenize":
            tokenize(file_contents, print_tokens=True)
        case "parse":
            parse(file_contents, print_stmts=True)
        case "evaluate":
            interpret(file_contents, print_output=True)
        case _:
            print(f"Unknown command: {command}", file=sys.stderr)
            exit(1)

def tokenize(file_contents, print_tokens=False):
    # Tokenize to get tokens
    scanner = Scanner(file_contents)
    tokens = scanner.scan_tokens()

    # Print tokens
    if print_tokens:
        for token in tokens:
            print(token)

    # Check code errors
    if Lox.hasError: exit(65)

    return tokens

def parse(file_contents, print_stmts=False):
    # Parse to get expr
    tokens = tokenize(file_contents)
    parser = Parser(tokens)
    stmts = parser.parse()

    # Check code errors
    if Lox.hasError: exit(65)

    # Print all statements
    if print_stmts:
        for stmt in stmts:
            print(stmt)

    return stmts

def interpret(file_contents, print_output=False):
    # Interpret to get output
    stmts = parse(file_contents)
    interpreter = Interpreter(stmts)
    outputs = interpreter.interpret()

    # Check code errors
    if Lox.hasRuntimeError: exit(70)

    # Print output and return it if it's an actual value
    if print_output:
        for output in outputs:
            print(output)
    
    return outputs

if __name__ == "__main__":
    main()
