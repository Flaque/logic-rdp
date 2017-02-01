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


# Create an Enum vocabulary
from enum import Enum
class Token(Enum):
    S = 1
    PROP = 2
    LOG = 3
    NEG = 4
    AND = 5
    OR = 6
    IMPL = 7
    EQ = 8
    END = 9

def getToken(string):
    """ Returns a token for a string """
    if len(string) == 1 and string.isalpha():
        return Token.PROP
    if string == "true" or string == "false":
        return Token.LOG
    if string == "not":
        return Token.NEG
    if string == "and":
        return Token.AND
    if string == "or":
        return Token.OR
    if string == "impl":
        return Token.IMPL
    if string == "=":
        return Token.EQ

    # Token doesn't exist!
    raise "Token %s doesn't exist." % (string)

words = "a and not b".split(" ")
tok = None

def consume():
    if words:
        tok = getToken(words.pop(0))
    else:
        tok = Token.END

def PROP():
    pass

def LOG():
    pass

def NEG():
    pass

def AND():
    pass

def OR():
    pass

def IMPL():
    pass

def EQ():
    pass

def S():

    consume()

    if tok == Token.PROP:
        PROP()
    if tok == Token.LOG:
        LOG()
    if tok == Token.NEG:
        NEG()
    if tok == Token.AND:
        AND()
    if tok == Token.OR:
        OR()
    if tok == Token.IMPL:
        IMPL()



print consume()
