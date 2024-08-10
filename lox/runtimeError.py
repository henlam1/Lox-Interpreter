
class RuntimeError(RuntimeError):
	def __init__(self, token, message) -> None:
		super().__init__(message)
		self.token = token
		self.message = message

def checkNumberOperand(operator, operand):
	if isinstance(operand, float): return
	raise RuntimeError(operator, "Operand must be a number.")

def checkNumberOperands(operator, left, right):
	if isinstance(left, float) and isinstance(right, float): return
	raise RuntimeError(operator, "Operands must be numbers.")