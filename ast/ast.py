class Node:
    def token_literal(self): pass


class Statement(Node)
    node = None

    def statement_node(self): pass


class Expression(Node):
    def expression_node(self): pass


class Program(Node):
    def __init__(self, prog=[])
        self.prog = prog  # program

    def token_literal(self):
        p = self
        if len(p.stmts) > 0:
            return p.stmts[0].token_literal()
        else:
            return ''


class LetStatement(Statement):
    def __init__(self, tok=None, name=None, val=None):
        self.tok = tok    # token
        self.name = name  # variable name
        self.val = val    # value

    def token_literal(self):
        ls = self
        return ls.tok.lit


class Identifier(Expression):
    def __init__(self, tok=None, val=None):
        self.tok = tok  # token
        self.val = val  # value

    def token_literal(self):
        i = self
        return i.tok.lit
