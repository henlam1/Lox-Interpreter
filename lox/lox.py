import sys
from .tokenType import TOKEN_TYPE

class Lox:
    # Class variables
    hasError = False
    hasRuntimeError = False

    def __init__(self) -> None:
        pass
    
    @staticmethod
    def scanError(line, message):
        Lox.report(line, "", message)
    
    @staticmethod
    def parseError(token, message):
        if token.type == TOKEN_TYPE.EOF:
            Lox.report(token.line, " at end", message)
        else:
            Lox.report(token.line, f" at {token.lexeme}", message)
    
    @staticmethod
    def runtimeError(error):
        print({f"{error.message}\nline {error.token.line}]"}, file=sys.stderr)
        Lox.hasRuntimeError = True

    @staticmethod
    def report(line, where, message):
        print(f"[line {line}] Error{where}: {message}", file=sys.stderr)
        Lox.hasError = True