from .lox import *
from .reserved import *
from .token import Token
from .tokenType import TOKEN_TYPE

class Scanner:
    def __init__(self, content):
        self.content = content
        self.start = 0
        self.current = 0
        self.line = 1
        self.tokens = []
    
    def peek(self):
        if self.is_at_end(): return "\0"
        return self.content[self.current]

    def peek_next(self):
        if self.current + 1 >= len(self.content): return "\0"
        return self.content[self.current + 1]
    
    def is_at_end(self):
        return self.current >= len(self.content)
    
    def advance(self):
        # Get character and then advance pointer
        c = self.content[self.current]
        self.current += 1

        return c
    
    def scan_tokens(self):
        # Scan tokens while there's still tokens
        while not self.is_at_end():
            self.start = self.current
            self.scan_token()
        
        # Append EOF at the end
        self.tokens.append(Token(TOKEN_TYPE.EOF, "", None, self.line))
        return self.tokens

    def scan_token(self):
        c = self.advance()
        if c == "(": self.add_token(TOKEN_TYPE.LEFT_PAREN)
        elif c == ")": self.add_token(TOKEN_TYPE.RIGHT_PAREN)
        elif c == "{": self.add_token(TOKEN_TYPE.LEFT_BRACE)
        elif c == "}": self.add_token(TOKEN_TYPE.RIGHT_BRACE)
        elif c == ",": self.add_token(TOKEN_TYPE.COMMA)
        elif c == ".": self.add_token(TOKEN_TYPE.DOT)
        elif c == "-": self.add_token(TOKEN_TYPE.MINUS)
        elif c == "+": self.add_token(TOKEN_TYPE.PLUS)
        elif c == ";": self.add_token(TOKEN_TYPE.SEMICOLON)
        elif c == "*": self.add_token(TOKEN_TYPE.STAR)
        elif c == "=": self.add_token(TOKEN_TYPE.EQUAL_EQUAL if self.match("=") else TOKEN_TYPE.EQUAL)
        elif c == "!": self.add_token(TOKEN_TYPE.BANG_EQUAL if self.match("=") else TOKEN_TYPE.BANG)
        elif c == "<": self.add_token(TOKEN_TYPE.LESS_EQUAL if self.match("=") else TOKEN_TYPE.LESS)
        elif c == ">": self.add_token(TOKEN_TYPE.GREATER_EQUAL if self.match("=") else TOKEN_TYPE.GREATER)
        elif c == "/": self.comment()
        elif c == "\"": self.string()
        elif c in [" ", "\t"]: pass
        elif c == "\n": self.line += 1
        elif self.is_digit(c): self.number()
        elif self.is_alpha(c): self.identifier()
        else: Lox.scanError(self.line, f"Unexpected character: {c}")

    def match(self, expected):
        # No more characters to match ahead
        if self.is_at_end():
            return False
        
        # Perform a 1 char lookahead (current is always ahead)
        if self.content[self.current] != expected:
            return False

        self.current += 1
        return True
    
    def comment(self):
        if self.match("/"):
            # Match comment content until end of the line or file ends
            while self.peek() != "\n" and not self.is_at_end():
                self.advance()
        else: self.add_token(TOKEN_TYPE.SLASH)
    
    def string(self):
        # Loop until we find closing quote
        while self.peek() != "\"" and not self.is_at_end():
            # Increment any new lines
            if self.peek() == "\n":
                self.line += 1
            self.advance()
            # Post advancement check
            if self.is_at_end():
                Lox.scanError(self.line, "Unterminated string.")
                return

        # Closing advance to capture last quote
        self.advance()
        literal = self.content[self.start + 1: self.current - 1]
        self.add_token(TOKEN_TYPE.STRING, literal)
    
    def is_digit(self, char):
        return char >= "0" and char <= "9"
    
    def number(self):
        # Loop for the first half of the number
        while self.is_digit(self.peek()):
            self.advance()
        
        # Check for fractional dot and digits following
        if self.peek() == "." and self.is_digit(self.peek_next()):
            self.advance()

        while self.is_digit(self.peek()):
            self.advance()
            
        literal = self.content[self.start:self.current]
        self.add_token(TOKEN_TYPE.NUMBER, float(literal))
    
    def is_alpha(self, char):
        return (char >= "a" and char <= "z" or
                char >= "A" and char <= "Z" or
                char == "_")

    def is_alphanumeric(self, char):
        return self.is_digit(char) or self.is_alpha(char)
    
    def identifier(self):
        # Extract the whole string
        while self.is_alphanumeric(self.peek()):
            self.advance()
        
        # Check if our string is a reserved word
        identifier = self.content[self.start : self.current]
        type = RESERVED.get(identifier, TOKEN_TYPE.IDENTIFIER)
        self.add_token(type)
        
    def add_token(self, type, literal=None):
        lexeme = self.content[self.start : self.current]
        self.tokens.append(Token(type, lexeme, literal, self.line))