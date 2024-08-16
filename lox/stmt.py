from .expr import Expr
from .token import Token

# Stmt interface for our tokens
class Stmt:
    class Visitor:
        def visitBlockStmt(self, stmts):
            pass

        def visitIfStmt(self, expr):
            pass

        def visitForStmt(self, expr):
            pass

        def visitPrintStmt(self, expr):
            pass

        def visitVarStmt(self, expr):
            pass

        def visitWhileStmt(self, expr):
            pass

        def visitExpressionStmt(self, expr):
            pass

    def accept(self, visitor):
        pass

class Block(Stmt):
    def __init__(self, stmts) -> None:
        self.stmts = stmts
    
    def accept(self, visitor: Stmt.Visitor):
        return visitor.visitBlockStmt(self)
    
    def __str__(self) -> str:
        return ""
    
class Expression(Stmt):
    def __init__(self, expr: Expr) -> None:
        self.expr = expr
    
    def accept(self, visitor: Stmt.Visitor):
        return visitor.visitExpressionStmt(self)
    
    def __str__(self) -> str:
        return str(self.expr)

class For(Stmt):
    def __init__(self, condition: Expr, body: Stmt) -> None:
        self.condition = condition
        self.body = body
    
    def accept(self, visitor: Stmt.Visitor):
        return visitor.visitForStmt(self)

    def __str__(self) -> str:
        return ""

class If(Stmt):
    def __init__(self, condition: Expr, thenBranch: Stmt, elseBranch: Stmt) -> None:
        self.condition = condition
        self.thenBranch = thenBranch
        self.elseBranch = elseBranch
    
    def accept(self, visitor: Stmt.Visitor):
        return visitor.visitIfStmt(self)
    
    def __str__(self) -> str:
        return ""
    
class Print(Stmt):
    def __init__(self, expr: Expr) -> None:
        self.expr = expr
    
    def accept(self, visitor: Stmt.Visitor):
        return visitor.visitPrintStmt(self)
    
    def __str__(self) -> str:
        return f"{self.expr}"

class While(Stmt):
    def __init__(self, condition: Expr, body: Stmt) -> None:
        self.condition = condition
        self.body = body
    
    def accept(self, visitor: Stmt.Visitor):
        return visitor.visitWhileStmt(self)

    def __str__(self) -> str:
        return ""

class Var(Stmt):
    def __init__(self, name: Token, initializer: Expr) -> None:
        self.name = name
        self.initializer = initializer
    
    def accept(self, visitor: Stmt.Visitor):
        return visitor.visitVarStmt(self)
    
    def __str__(self) -> str:
        return ""