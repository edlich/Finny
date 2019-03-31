# (C) 2016, Stefan Edlich, Apache 2 License
import chess

mtime = 0 # movetime set by the 
goparams = [] # Could be ...

def cmain(tuple): # board, 1462484917.8764188, ['c2c4', 'c7c5'],['depth', '4']
  global board, mtime, line, goparams
  board = tuple[0]
  mtime = tuple[1]
  line = tuple[2]
  goparams = tuple[3]

  board.push(chess.Move.from_uci(line[-1]))
  print(board)
  print("-------------------")

  counter = 0
  mlist = []
  for move in board.legal_moves:
    counter += 1
    mlist.append(move)

  print("counter=", counter)
  print("move 5=", mlist[5])

  board.push(mlist[0])
  print("bestmove", "e7e6") # mlist.len()-2
  print(board)


