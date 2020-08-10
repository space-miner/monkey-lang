from ast import ast
from tok import token
from lex import lexer


class Parser:
    def __init__(self, l=None, ctok=None, ptok=None):
        self.l = l
        self.ctok = ctok  # current token
        self.ptok = ptok  # peek token

    def next_token(self):
        p = self
        p.ctok = p.ptok
        p.ptok = p.l.next_token()

    def parse_program(self):
        p = self
        program = ast.Program()
        while p.ctok.typ != token.EOF:
            stmt = p.parse_statement()
            if stmt is not None:
                program.prog.append(stmt)
        return prog

    def parse_statement(self):
        p = self
        if p.ctok.typ == token.LET:
            stmt = p.parse_let()
        elif p.ctok.typ == token.RETURN:
            stmt = p.parse_return()
        elif p.ctok.typ == token.IF:
            stmt = p.parse_if()
        return stmt

    def parse_let(self):
        p = self
        p.next_token()
        identifier = p.parse_identifier()
        p.next_token()
        if p.ctok != token.ASSIGN:
            print('no equal sign!')
            return None
        p.next_token()
        value = p.parse_expression()
        return ast.LetStatement(token.LET, identifier, value)

    def parse_identifier(self):
        p = self
        return ast.Identifier(p.ctok)

    def parse_expression(self):
        p = self
        pass


def new(self, l):
    p = Parser(l)
    # read two tokens, ctok and ptok
    p.next_token()
    p.next_token()
    return p
