from .tokens import *

RESERVED = {
    "and":    TOKEN_TYPE.AND,
    "class":  TOKEN_TYPE.CLASS,
    "else":   TOKEN_TYPE.ELSE,
    "false":  TOKEN_TYPE.FALSE,
    "for":    TOKEN_TYPE.FOR,
    "fun":    TOKEN_TYPE.FUN,
    "if":     TOKEN_TYPE.IF,
    "nil":    TOKEN_TYPE.NIL,
    "or":     TOKEN_TYPE.OR,
    "print":  TOKEN_TYPE.PRINT,
    "return": TOKEN_TYPE.RETURN,
    "super":  TOKEN_TYPE.SUPER,
    "this":   TOKEN_TYPE.THIS,
    "true":   TOKEN_TYPE.TRUE,
    "var":    TOKEN_TYPE.VAR,
    "while":  TOKEN_TYPE.WHILE,
}