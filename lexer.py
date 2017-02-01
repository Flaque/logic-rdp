from token import Token

class Lexer:

    __init__(self, string):
        self.tokens = string.split(' ') # Tokens must be split by spaces

    nextToken(self):

        # End of file!
        if not self.tokens:
            return Token.END

        # Grab next token
        tok = self.tokens.pop(0)

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
