from .token import Token

class Environment:
    def __init__(self) -> None:
        self.map = {}
        
    def define(self, name: Token, value: object) -> None:
        self.map[name] = value
    
    def get(self, name: Token):
        if name.lexeme in self.map:
            return self.map[name.lexeme]
        raise RuntimeError(name, f"Undefined variable '{name.lexeme}'.")