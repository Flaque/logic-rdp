from parser import Parser

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


grammar = """
----------------------------------------------
S    : PROP | LOG | NEG | AND | OR | IMPL | EQ
PROP : a | b | c | ... | z
LOG  : true | false
NEG  : not S
AND  : S and S
OR   : S or S
IMPL : S impl S
EQ   : S = S
----------------------------------------------

"""

parser = Parser()
header = bcolors.HEADER + "Welcome to our A+ worthy parser!\n" + bcolors.ENDC
prompt = header + """You can either:
1. Enter a string you would like to parse.
2. Enter "grammar" to see the language grammar
3. Enter "end" to quit.

type your input below:
"""

user_input = ""

while user_input != "end":
    user_input = raw_input(prompt)
    if user_input == "end":
        print bcolors.OKBLUE + "bye!" + bcolors.ENDC
        break

    if user_input == "grammar":
        print grammar
        continue

    isCorrect = parser.run(user_input)
    if isCorrect:
        print bcolors.OKGREEN + "\nAnswer: yes\n" + bcolors.ENDC
    else:
        print bcolors.FAIL + "\nAnswer: no\n" + bcolors.ENDC
