from tok import token


class Lexer:
    def __init__(self, inp='', pos=0, rpos=0, ch=''):
        self.inp = inp
        self.pos = pos
        self.rpos = rpos
        self.ch = ch

    def next_token(self):
        l = self
        if l.ch == '=':
            tok = new_token(token.ASSIGN, l.ch)
        elif l.ch == ';':
            tok = new_token(token.SEMICOLON, l.ch)
        elif l.ch == '(':
            tok = new_token(token.LPAREN, l.ch)
        elif l.ch == ')':
            tok = new_token(token.RPAREN, l.ch)
        elif l.ch == ',':
            tok = new_token(token.COMMA, l.ch)
        elif l.ch == '+':
            tok = new_token(token.PLUS, l.ch)
        elif l.ch == '{':
            tok = new_token(token.LBRACE, l.ch)
        elif l.ch == '}':
            tok = new_token(token.RBRACE, l.ch)
        elif l.ch == '0':
            tok = new_token(token.EOF, '')
        else:
            if is_letter(l.ch):
                lit = l.read_identifier()
                typ = token.lookup_identifier(lit)
                tok = new_token(typ, lit)
            elif is_digit(l.ch):
                lit = l.read_number()
                typ = token.INT
                tok = new_token(typ, lit)
            else:
                tok = new_token(token.ILLEGAL, l.ch)
        l.read_char()
        print(tok.typ, tok.lit)
        return tok

    def read_char(self):
        l = self
        if l.rpos >= len(l.inp):
            l.ch = 0
        else:
            l.ch = l.inp[l.rpos]
        l.pos = l.rpos
        l.rpos += 1

    def read_identifier(self):
        l = self
        pos = l.pos
        while is_letter(l.ch):
            l.read_char()
        return l.inp[pos:l.pos]

    def read_number(self):
        l = self
        pos = l.pos
        while l.ch != 0 and is_digit(l.ch):
          l.read_char()
        return l.inp[pos:l.pos]


def is_digit(ch):
    return '0' <= ch <= '9'


def is_letter(ch):
    return 'A' <= ch <= 'z' or ch == '_'


def new(inp):
    l = Lexer(inp)
    l.read_char()
    return l


def new_token(typ, ch):
    return token.Token(typ, ch)
