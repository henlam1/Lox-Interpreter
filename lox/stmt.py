# Stmt interface for our tokens
class Stmt:
    class Visitor:
        def visitExpressionStmt(self, expr):
            pass

        def visitPrintStmt(self, expr):
            pass

    def accept(self, visitor):
        pass

class Expression(Stmt):
    def __init__(self, expr) -> None:
        self.expr = expr
    
    def accept(self, visitor: Stmt.Visitor):
        return visitor.visitExpressionStmt(self)
    
    def __str__(self) -> str:
        return f"{self.expr}"
    
class Print(Stmt):
    def __init__(self, expr) -> None:
        self.expr = expr
    
    def accept(self, visitor: Stmt.Visitor):
        return visitor.visitPrintStmt(self)
    
    def __str__(self) -> str:
        return f"{self.expr}"