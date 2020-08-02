class Lexer:
  def __init__(self, inp='', pos=0, rpos=0, ch=''):
    self.inp = inp
    self.pos = pos
    self.rpos = rpos
    self.ch = ch

def new(inp):
  l = Lexer(inp)
  l.read_char()
  return l
