ILLEGAL = "ILLEGAL"
EOF = "EOF"

IDENT = "IDENT"
INT = "INT"

ASSIGN = "ASSIGN"
PLUS = "PLUS"

COMMA = "COMMA"
SEMICOLON = "SEMICOLON"

LPAREN = "LPAREN"
RPAREN = "RPAREN"
LBRACE = "LBRACE"
RBRACE = "RBRACE"

FUNCTION = "FUNCTION"
LET = "LET"


class Token:
    def __init__(self, typ, lit):
        self.typ = typ
        self.lit = lit


keywords = {
    'fn': FUNCTION,
    'let': LET,
}


def lookup_identifier(ident):
    if ident in keywords:
        return keywords[ident]
    return IDENT
