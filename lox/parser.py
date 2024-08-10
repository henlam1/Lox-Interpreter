from .tokens import *
from .expr import *
from .lox import *

class ParseError(RuntimeError):
    pass

class Parser:
    def __init__(self, tokens) -> None:
        self.tokens = tokens
        self.current = 0
    
    def parse(self):
        try:
            return self.expression()
        except ParseError:
            return None
    
    def expression(self):
        return self.equality()
    
    def equality(self):
        expr = self.comparison()

        while self.match(TOKEN_TYPE.BANG_EQUAL, TOKEN_TYPE.EQUAL_EQUAL):
            operator = self.previous()
            right = self.comparison()
            expr = Binary(expr, operator, right)

        return expr
    
    def comparison(self):
        expr = self.term()

        while self.match(TOKEN_TYPE.GREATER, TOKEN_TYPE.GREATER_EQUAL,
                         TOKEN_TYPE.LESS, TOKEN_TYPE.LESS_EQUAL):
            operator = self.previous()
            right = self.term()
            expr = Binary(expr, operator, right)
        
        return expr

    def term(self):
        expr = self.factor()

        while self.match(TOKEN_TYPE.MINUS, TOKEN_TYPE.PLUS):
            operator = self.previous()
            right = self.factor()
            expr = Binary(expr, operator, right)
        
        return expr
    
    def factor(self):
        expr = self.unary()

        while self.match(TOKEN_TYPE.SLASH, TOKEN_TYPE.STAR):
            operator = self.previous()
            right = self.unary()
            expr = Binary(expr, operator, right)
        
        return expr
    
    def unary(self):
        if self.match(TOKEN_TYPE.BANG, TOKEN_TYPE.MINUS):
            operator = self.previous()
            right = self.unary()
            return Unary(operator, right)
        
        return self.primary()
    
    def primary(self):
        if self.match(TOKEN_TYPE.FALSE): return Literal(False)
        if self.match(TOKEN_TYPE.TRUE): return Literal(True)
        if self.match(TOKEN_TYPE.NIL): return Literal(None)

        if self.match(TOKEN_TYPE.NUMBER, TOKEN_TYPE.STRING): 
            return Literal(self.previous().literal) # Token.literal

        if self.match(TOKEN_TYPE.LEFT_PAREN):
            # Error if empty expression
            expr = self.expression()
            if not expr:
                self.error(self.peek(), "Missing expr")

            self.consume(TOKEN_TYPE.RIGHT_PAREN, "Expect ')' after expression.")
            return Grouping(expr)

        raise self.error(self.peek(), "Expect expression.")
    
    def consume(self, token_type, err_msg):
        if self.check(token_type):
            return self.advance()
        
        # Error if unmatched parenthesis
        raise self.error(self.peek(), err_msg)
        
    def match(self, *types):
        # Try to match all tokens until it is found
        for token_type in types:
            if self.check(token_type):
                self.advance()
                return True
        
        return False

    def check(self, token):
        if self.is_at_end(): return False
        return self.peek().type == token

    def advance(self):
        token = self.tokens[self.current]
        self.current += 1
        return token

    def is_at_end(self):
        return self.peek().type == TOKEN_TYPE.EOF

    def peek(self):
        return self.tokens[self.current]
    
    def previous(self):
        return self.tokens[self.current - 1]
    
    def error(self, token, message):
        Lox.parseError(token, message)
        return ParseError()