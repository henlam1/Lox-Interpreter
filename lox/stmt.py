from .expr import Expr
from .token import Token

# Stmt interface for our tokens
class Stmt:
    class Visitor:
        def visitExpressionStmt(self, expr):
            pass

        def visitPrintStmt(self, expr):
            pass

        def visitVarStmt(self, expr):
            pass

    def accept(self, visitor):
        pass

class Expression(Stmt):
    def __init__(self, expr: Expr) -> None:
        self.expr = expr
    
    def accept(self, visitor: Stmt.Visitor):
        return visitor.visitExpressionStmt(self)
    
    def __str__(self) -> str:
        return f"{self.expr}"
    
class Print(Stmt):
    def __init__(self, expr: Expr) -> None:
        self.expr = expr
    
    def accept(self, visitor: Stmt.Visitor):
        return visitor.visitPrintStmt(self)
    
    def __str__(self) -> str:
        return f"{self.expr}"

class Var(Stmt):
    def __init__(self, name: Token, initializer: Expr) -> None:
        self.name = name
        self.initializer = initializer
    
    def accept(self, visitor: Stmt.Visitor):
        return visitor.visitVarStmt(self)
    
    def __str__(self) -> str:
        return f"{self.name} = {self.initializer}"