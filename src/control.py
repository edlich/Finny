# (C) 2016, Stefan Edlich, Apache 2 License

mtime = 0 # movetime set by the 
goparams = [] # Could be ...

def cmain(tuple): # 1462484917.8764188, ['c2c4', 'c7c5'],['depth', '4']
  global mtime, line, goparams
  mtime = tuple[0]
  line = tuple[1]
  goparams = tuple[2]

  print("bestmove", "g8f6")


