from .token import Token

class Environment:
    def __init__(self, enclosing: 'Environment'=None) -> None:
        self.map = {}
        self.enclosing = enclosing
        
    def define(self, name: Token, value: object) -> None:
        self.map[name] = value
    
    def get(self, name: Token):
        # Check if the name is in this environment
        if name.lexeme in self.map:
            return self.map[name.lexeme]
        
        # Search upwards for var in the chain of environments
        if self.enclosing:
            return self.enclosing.get(name)

        raise RuntimeError(name, f"Undefined variable '{name.lexeme}'.")
    
    def assign(self, name: Token, value: object):
        # Check if the name is in this environment
        if name.lexeme in self.map:
            self.map[name.lexeme] = value
            return
        
        # Search upwards for var in the chain of environments
        if self.enclosing:
            self.enclosing.assign(name, value)
            return
        
        raise RuntimeError(name, f"Undefined variable '{name.lexeme}'.")