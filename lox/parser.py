from .lox import Lox
from .expr import *
from .stmt import *
from .tokenType import TOKEN_TYPE

class ParseError(RuntimeError):
    pass

class Parser:
    def __init__(self, tokens) -> None:
        self.tokens = tokens
        self.current = 0
        
    def parse(self):
        statements = []
        while not self.is_at_end():
            statements.append(self.declaration())
        return statements
    
    def declaration(self):
        try: 
            if self.match(TOKEN_TYPE.VAR):
                return self.varDeclaration()
            return self.statement()
        except ParseError:
            self.synchronize()
            return None
    
    def varDeclaration(self):
        name = self.consume(TOKEN_TYPE.IDENTIFIER, "Expect variable name.")
        # Initializers can have/not have values. 
        # Ex: var x; OR var x = 1;
        initializer = None
        if self.match(TOKEN_TYPE.EQUAL):
            initializer = self.expression()
        
        self.consume(TOKEN_TYPE.SEMICOLON, "Expect ';' after variable declaration")
        return Var(name, initializer)
        
    def statement(self):
        if self.match(TOKEN_TYPE.LEFT_BRACE):
            return Block(self.block())
        if self.match(TOKEN_TYPE.PRINT):
            return self.printStatement()
        return self.expressionStatement()
    
    def printStatement(self):
        value = self.expression()
        self.consume(TOKEN_TYPE.SEMICOLON, "Expect ';' after value.")
        return Print(value)
    
    def expressionStatement(self):
        expr = self.expression()
        self.consume(TOKEN_TYPE.SEMICOLON, "Expect ';' after value.")
        return Expression(expr)
    
    def block(self):
        # Build list of statements
        stmts = []
        while not self.check(TOKEN_TYPE.RIGHT_BRACE) and not self.is_at_end():
            stmts.append(self.declaration())

        self.consume(TOKEN_TYPE.RIGHT_BRACE, "Expect '}' after block.")
        return stmts
        
    def expression(self):
        return self.assignment()
    
    def assignment(self):
        expr = self.equality()
        if self.match(TOKEN_TYPE.EQUAL):
            equals = self.previous()
            value = self.assignment()
        
            if isinstance(expr, Variable):
                name = expr.name
                return Assign(name, value)

            self.error(equals, "Invalid assignment target.")

        return expr
    
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
        # Booleans
        if self.match(TOKEN_TYPE.FALSE): return Literal(False)
        if self.match(TOKEN_TYPE.TRUE): return Literal(True)
        if self.match(TOKEN_TYPE.NIL): return Literal(None)

        # Literals
        if self.match(TOKEN_TYPE.NUMBER, TOKEN_TYPE.STRING): 
            return Literal(self.previous().literal) # Token.literal

        # Expressions
        if self.match(TOKEN_TYPE.LEFT_PAREN):
            # Error if empty expression
            expr = self.expression()
            if not expr:
                self.error(self.peek(), "Missing expr")

            self.consume(TOKEN_TYPE.RIGHT_PAREN, "Expect ')' after expression.")
            return Grouping(expr)
        
        # Identifiers
        if self.match(TOKEN_TYPE.IDENTIFIER):
            return Variable(self.previous())

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
    
    def synchronize(self):
        self.advance()

        # Keep advancing tokens until we're at a new statement
        while not self.is_at_end():
            # We're at a new statement if we went past a semicolon
            if self.previous().type == TOKEN_TYPE.SEMICOLON:
                return
            
            # We're at a new statement if it starts with a keyword
            tokenType = self.peek().type
            keywords = set([TOKEN_TYPE.CLASS, TOKEN_TYPE.FUN, 
                           TOKEN_TYPE.VAR, TOKEN_TYPE.FOR,
                           TOKEN_TYPE.IF, TOKEN_TYPE.WHILE,
                           TOKEN_TYPE.PRINT, TOKEN_TYPE.RETURN])
            if tokenType in keywords:
                return
            
            self.advance()

