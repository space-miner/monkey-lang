class Lexer:
  def __init__(self, inp='', pos=0, rpos=0, ch=''):
    self.inp = inp
    self.pos = pos
    self.rpos = rpos
    self.ch = ch

  def read_char(self):
    l = self
    if l.rpos >= len(l.inp):
      l.ch = 0
    else:
      l.ch = l.inp[l.rpos]
    l.pos = l.rpos
    l.rpos += 1

def new(inp):
  l = Lexer(inp)
  l.read_char()
  return l
