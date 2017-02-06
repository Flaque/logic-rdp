#
#  Programmers: Evan Conrad, Abdullah Alhassan, Sebastien, Andrea
#  filename:    token.py
#  Date:        02/06/2017
#  Class:       Artificial Intelegence CPSC 427
#

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
