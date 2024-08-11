from .tokens import *
from .expr import *
from .stmt import *
from .runtimeError import *
from .lox import *

class Interpreter(Expr.Visitor):
    def __init__(self, stmts: list[Stmt]) -> None:
        self.stmts = stmts
    
    def interpret(self):
        # FIX THIS. I'm only executing and not returning a value
        # For now, unsure how to differentiate between null value from prints and actual value from exprStmts
        try:
            for stmt in self.stmts:
                value = self.execute(stmt)
            return self.fixValue(value)
        except RuntimeError as r:
            Lox.runtimeError(r)
    
    def fixValue(self, value):
        # Convert bools
        if value is None: return "nil"
        if isinstance(value, bool): return str(value).lower()

        # Convert floats to ints
        if isinstance(value, float): 
            if value.is_integer(): return str(int(value))
            return str(value)

        # Return strings
        return value

    def isTruthy(self, obj):
        if obj is None: return False
        if isinstance(obj, bool): return obj
        return True
    
    def evaluate(self, expr: Expr):
        return expr.accept(self)
    
    def execute(self, stmt: Stmt):
        return stmt.accept(self)
    
    # STATEMENT VISITORS
    def visitExpressionStmt(self, stmt: Expression):
        value = self.evaluate(stmt.expr)
        return value
    
    def visitPrintStmt(self, stmt: Print):
        value = self.evaluate(stmt.expr)
        print(self.fixValue(value))
        return 
    
    # EXPR VISITORS
    def visitLiteralExpr(self, expr: Literal):
        return expr.value
    
    def visitGroupingExpr(self, expr: Grouping):
        return self.evaluate(expr.expr)

    def visitUnaryExpr(self, expr: Unary):
        right = self.evaluate(expr.right)

        match expr.operator.type:
            case TOKEN_TYPE.BANG:
                return not self.isTruthy(right)
            case TOKEN_TYPE.MINUS:
                checkNumberOperand(expr.operator, right)
                return -right
            case _:
                return None
    
    def visitBinaryExpr(self, expr: Binary):
        left = self.evaluate(expr.expr)
        right = self.evaluate(expr.right)

        # Order of PEMDAS reversed
        match expr.operator.type:
            # Unary
            case TOKEN_TYPE.BANG_EQUAL:
                return not (left == right)
            case TOKEN_TYPE.EQUAL_EQUAL:
                return left == right
            # Comparison
            case TOKEN_TYPE.GREATER:
                checkNumberOperands(expr.operator, left, right)
                return left > right
            case TOKEN_TYPE.GREATER_EQUAL:
                checkNumberOperands(expr.operator, left, right)
                return left >= right
            case TOKEN_TYPE.LESS:
                checkNumberOperands(expr.operator, left, right)
                return left < right
            case TOKEN_TYPE.LESS_EQUAL:
                checkNumberOperands(expr.operator, left, right)
                return left <= right
            # Arithmetic
            case TOKEN_TYPE.MINUS:
                checkNumberOperands(expr.operator, left, right)
                return left - right
            case TOKEN_TYPE.PLUS:
                if ((isinstance(left, float) and isinstance(right, float)) or
                    (isinstance(left, str) and isinstance(right, str))):
                        return left + right
                raise RuntimeError(expr.operator, "Operands must be numbers or strings")
            case TOKEN_TYPE.SLASH:
                checkNumberOperands(expr.operator, left, right)
                if right == 0:
                    raise RuntimeError(expr.operator, "Division by zero error!")
                return left / right
            case TOKEN_TYPE.STAR:
                checkNumberOperands(expr.operator, left, right)
                return left * right