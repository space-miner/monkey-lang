import getpass
import os
import sys
sys.path.append(os.path.abspath('./'))
from tok import token
from lex import lexer

prompt = '>>'


def main():
    user = getpass.getuser()
    print(f"Hello {user}! This is the Monkey programming language!")
    print("Feel free to type in commands")
    prog = []
    line = input(prompt)
    while line:
        prog.append(line)
        line = input(prompt)
    inp = ' '.join(prog)
    l = lexer.new(inp)
    tok = l.next_token()
    while tok.typ != token.EOF:
        print(f"type - {tok.typ}\nliteral - {tok.lit}\n")
        tok = l.next_token()


if __name__ == '__main__':
    main()
