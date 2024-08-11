class Token:
    def __init__(self, type, lexeme, literal, line):
        self.type = type    # String version
        self.lexeme = lexeme    # Actual character
        self.literal = literal  # Literal value (e.g 21)
        self.line = line

        # Modify literal
        if self.literal is None:
            self.literal = "null"

    def __str__(self):
        return f"{self.type.name} {self.lexeme} {self.literal}"