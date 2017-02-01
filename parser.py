#
# A recursive descent parser for logic
#
# --------------------------------------------
# S : PROP | LOG | NEG | AND | OR | IMPL | EQ
# PROP : a | b | c | ... | z
# LOG : true | false
# NEG : not S
# AND : S and
# OR : S or S
# IMPL : S impl S
# EQ : S = S
# --------------------------------------------

from token import Token
import Lexer

lexer = None
tok = None

def run(string):
    lexer = Lexer(string)
    tok = lexer.nextToken()
    return S()

def nextToken():
    tok = lexer.nextToken()

def expect(token_type):
    nextToken()
    if tok != token_type:
        raise "was expecting a %s" % (token_type)

def EQ():
    S()

def S():
    if tok is not Token.END:
        if not tok:
            return False # Something went wrong!

            if tok == Token.NEG:
                NEG()

    else return True; # We got to the end of the file with no problems!
