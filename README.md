
# A recursive descent parser for logic

By Evan Conrad, Abdullah Alhassan, Sebastien, Andrea

## Logic Rules

```
S    : PROP | LOG | NEG | AND | OR | IMPL | EQ
PROP : a | b | c | ... | z
LOG  : true | false
NEG  : not S
AND  : S and
OR   : S or S
IMPL : S impl S
EQ   : S = S
```

## To use

Run `python main.py` to test out our parser!
