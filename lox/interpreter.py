from .environment import Environment
from .expr import *
from .lox import Lox
from .runtimeError import RuntimeError, checkNumberOperand, checkNumberOperands
from .stmt import *
from .tokenType import TOKEN_TYPE

class Interpreter(Expr.Visitor):
    def __init__(self, stmts: list[Stmt]) -> None:
        self.environment = Environment()
        self.stmts = stmts
        self.outputs = []
    
    def interpret(self):
        try:
            for stmt in self.stmts:
                # Keep values from exprStmts
                value = self.execute(stmt)
                if isinstance(stmt, Expression):
                    self.outputs.append(self.fixValue(value))
            return self.outputs
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
    def executeBlock(self, stmts: list, newEnv: Environment):
        # Replace current env with block's env
        prevEnv = self.environment
        self.environment = newEnv
        try:
            for stmt in stmts:
                self.execute(stmt)
        finally:
            # Restore previous env
            self.environment = prevEnv
            
    def visitBlockStmt(self, stmt: Block):
        self.executeBlock(stmt.stmts, Environment(self.environment))
    
    def visitForStmt(self, stmt: For):
        pass
    
    def visitIfStmt(self, stmt: If):
        # Check the truthiness of condition
        value = self.evaluate(stmt.condition)
        if self.isTruthy(value):
            self.execute(stmt.thenBranch)
        elif stmt.elseBranch:
            self.execute(stmt.elseBranch)
        return None
    
    def visitPrintStmt(self, stmt: Print):
        value = self.evaluate(stmt.expr)
        print(self.fixValue(value))
    
    def visitVarStmt(self, stmt: Var):
        # Assign var value to value
        value = None
        if stmt.initializer:
            value = self.evaluate(stmt.initializer)
        self.environment.define(stmt.name.lexeme, value)
    
    def visitWhileStmt(self, stmt: While):
        while self.isTruthy(self.evaluate(stmt.condition)):
            self.execute(stmt.body)
        return None
    
    def visitExpressionStmt(self, stmt: Expression):
        value = self.evaluate(stmt.expr)
        return value
    
    # EXPR VISITORS
    def visitAssignExpr(self, expr: Assign):
        value = self.evaluate(expr.value)
        self.environment.assign(expr.name, value)
        return value
    
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
    
    def visitGroupingExpr(self, expr: Grouping):
        return self.evaluate(expr.expr)
    
    def visitLiteralExpr(self, expr: Literal):
        return expr.value

    def visitLogicalExpr(self, expr: Logical):
        left = self.evaluate(expr.left)
        if expr.operator.type == TOKEN_TYPE.OR:
            # Short circuit if left is true
            if self.isTruthy(left):
                return left
        else:
            # Short circuit if left is false
            if not self.isTruthy(left):
                return left
        
        return self.evaluate(expr.right)
    
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
    
    def visitVariableExpr(self, expr: Variable):
        return self.environment.get(expr.name)