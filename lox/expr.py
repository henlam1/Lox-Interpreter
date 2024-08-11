from .token import Token
# Expr interface for our tokens
class Expr:
    class Visitor:
        def visitBinaryExpr(self, expr):
            pass

        def visitGroupExpr(self, expr):
            pass

        def visitLiteralExpr(self, expr):
            pass

        def visitUnaryExpr(self, expr):
            pass

        def visitVariableExpr(self, expr):
            pass

    def accept(self, visitor):
        pass

class Binary(Expr):
    def __init__(self, expr: Expr, operator: Token, right: Expr) -> None:
        self.expr = expr
        self.operator = operator
        self.right = right
    
    def accept(self, visitor: Expr.Visitor):
        return visitor.visitBinaryExpr(self)
    
    def __str__(self) -> str:
        return f"({self.operator.lexeme} {self.expr} {self.right})"

class Grouping(Expr):
    def __init__(self, expr: Expr) -> None:
        self.expr = expr

    def accept(self, visitor: Expr.Visitor):
        return visitor.visitGroupingExpr(self)
    
    def __str__(self) -> str:
        return f"(group {self.expr})"

class Literal(Expr):
    def __init__(self, value: object) -> None:
        self.value = value
    
    def accept(self, visitor: Expr.Visitor):
        return visitor.visitLiteralExpr(self)
    
    def __str__(self) -> str:
        if self.value is None: return "nil"
        return str(self.value).lower()

class Unary(Expr):
    def __init__(self, operator: Token, right: Expr) -> None:
        self.operator = operator
        self.right = right
    
    def accept(self, visitor: Expr.Visitor):
        return visitor.visitUnaryExpr(self)
    
    def __str__(self) -> str:
        return f"({self.operator.lexeme} {self.right})"
    
class Variable(Expr):
    def __init__(self, name: str) -> None:
        self.name = name
    
    def accept(self, visitor: Expr.Visitor):
        return visitor.visitVariableExpr(self)

    def __str__(self) -> str:
        return f"{self.name}"