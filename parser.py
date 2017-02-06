#
#  Programmers: Evan Conrad, Abdullah Alhassan, Sebastien, Andrea
#  filename:    parser.py
#  Date:        02/06/2017
#  Class:       Artificial Intelegence CPSC 427
#
# A recursive descent parser for logic
#
# --------------------------------------------
# S : PROP | LOG | NEG | AND | OR | IMPL | EQ
# PROP : a | b | c | ... | z
# LOG : true | false
# NEG : not S
# AND : S and S
# OR : S or S
# IMPL : S impl S
# EQ : S = S
# --------------------------------------------

from token import Token
from lexer import Lexer

class Parser():

    def __init__(self):
        self.lexer = None
        self.tok = None

    def nextToken(self):
        self.tok = self.lexer.nextToken()

    def expect(self, token_type):
        self.nextToken()
        if self.tok != token_type:
            raise "was expecting a %s" % (token_type)

    def run(self, string):
        self.lexer = Lexer(string)
        return self.S()

    def S(self):
        self.nextToken()
        if self.tok is not Token.END:
            if not self.tok:
                return False # Something went wrong!

            return self.S()

        else:
            return True; # We got to the end of the file with no problems!

parser = Parser()

# Test whitespace
assert parser.run("a")        == True
assert parser.run("a  ")      == True
assert parser.run("  z")      == True
assert parser.run("b   or a") == True

# Test tokens
assert parser.run("b and a")  == True
assert parser.run("b impl a") == True
assert parser.run("z or a")   == True
assert parser.run("z = a")    == True
assert parser.run("z = true") == True
assert parser.run("false")    == True
assert parser.run("not a")    == True

# Test failure cases
assert parser.run("band a")   == False
assert parser.run("b blah a") == False
assert parser.run("1 and 2")  == False

# Test blocks
assert parser.run("a or b and c")        == True
assert parser.run("a impl b and c or z") == True
