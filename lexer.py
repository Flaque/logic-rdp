#
#  Programmers: Evan Conrad, Abdullah Alhassan, Sebastien, Andrea
#  filename:    lexer.py
#  Date:        02/06/2017
#  Class:       Artificial Intelegence CPSC 427
#
from token import Token

class Lexer:

    def __init__(self, string):
        self.tokens = string.strip().split(' ') # Tokens must be split by spaces

    def nextToken(self):

        # End of file!
        if not self.tokens:
            return Token.END

        # Grab next token
        tok = self.tokens.pop(0)

        # Ignore empty strings that can happen if the user puts too many
        # spaces in between their tokens
        if tok == "":
            return self.nextToken()

        if len(tok) == 1 and tok.isalpha():
            return Token.PROP
        if tok == "true" or tok == "false":
            return Token.LOG
        if tok == "not":
            return Token.NEG
        if tok == "and":
            return Token.AND
        if tok == "or":
            return Token.OR
        if tok == "impl":
            return Token.IMPL
        if tok == "=":
            return Token.EQ
        else:
            return None # Undefined
