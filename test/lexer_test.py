import unittest
import os
import sys
sys.path.append(os.path.abspath('../'))

from tok import token
from lex import lexer


class LexerTest(unittest.TestCase):
    def setUp(self):
        self.inp = '''let five = 5;
                   let ten = 10;
                   let add = fn(x, y) {
                     x + y;
                   };
                   let result = add(five, ten);
                   '''
        self.l = lexer.new(self.inp)

    def test_next_token(self):
        tests = [
            (token.LET, "let"),
            (token.IDENT, "five"),
            (token.ASSIGN, "="),
            (token.INT, "5"),
            (token.SEMICOLON, ";"),
            (token.LET, "let"),
            (token.IDENT, "ten"),
            (token.ASSIGN, "="),
            (token.INT, "10"),
            (token.SEMICOLON, ";"),
            (token.LET, "let"),
            (token.IDENT, "add"),
            (token.ASSIGN, "="),
            (token.FUNCTION, "fn"),
            (token.LPAREN, "("),
            (token.IDENT, "x"),
            (token.COMMA, ","),
            (token.IDENT, "y"),
            (token.RPAREN, ")"),
            (token.LBRACE, "{"),
            (token.IDENT, "x"),
            (token.PLUS, "+"),
            (token.IDENT, "y"),
            (token.SEMICOLON, ";"),
            (token.RBRACE, "}"),
            (token.SEMICOLON, ";"),
            (token.LET, "let"),
            (token.IDENT, "result"),
            (token.ASSIGN, "="),
            (token.IDENT, "add"),
            (token.LPAREN, "("),
            (token.IDENT, "five"),
            (token.COMMA, ","),
            (token.IDENT, "ten"),
            (token.RPAREN, ")"),
            (token.SEMICOLON, ";"),
        ]
        for t in tests:
            tok = self.l.next_token()
            self.assertEqual(tok.typ, t[0],
                             msg=f"{t} - tokentype wrong. expected={t[0]}, got={tok.typ}")
            self.assertEqual(tok.lit, t[1],
                             msg=f"{t} - literal wrong. expected={t[1]}, got={tok.lit}")


if __name__ == '__main__':
    unittest.main()
