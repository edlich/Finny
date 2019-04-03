# (C) 2016, Stefan Edlich, Apache 2 License
import chess
from random import randint

mtime = 0 # movetime set by the 
goparams = [] # Could be ...

def cmain(tuple): # board, 1462484917.8764188, ['c2c4', 'c7c5'],['depth', '4']
  global board, mtime, line, goparams
  board = tuple[0]
  mtime = tuple[1]
  line = tuple[2]
  goparams = tuple[3]

  if len(line)> 0: # Check if Finny has white in startpos because line = []
    board.push(chess.Move.from_uci(line[-1]))
  print(board)
  print("-------------------\n")

  mlist = list(board.legal_moves)
  print("type=",type(mlist))
  print("type=",len(mlist))
  the_move = mlist[randint(0,len(mlist))-1]

  board.push(the_move)
  print("bestmove", the_move)
  print(board)
