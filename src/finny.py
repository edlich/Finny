# (C) 2019, Stefan Edlich, Apache 2 License
# Main entry point for the chess program and UCI command processing

import sys
import time
import chess # https://github.com/niklasf/python-chess
from control import controller

line = None # save the move line for go
board = None

def quit(clist):
  sys.exit()

def uci(clist):
  print("id name FINNY 0.1") # Command 1/3 real version number!
  print("id author Stefan Edlich") # Command 2/3
  print("uciok") ## do not forget!! # Command 3/3

def isready(clist): #sync engine + gui
  print("readyok")

def ucinewgame(clist): # init engine. No answer required
  global board 
  board = chess.Board()
  print(">>> finny initialized")

def position(clist): # position startpos moves e2e4 e7e5 | position startpos | position fen 'fen'
  global line 
  if clist[0] == 'startpos':
    clist.pop(0) # remove startpos or fen
    # if not clist:
    if len(clist) != 0: # position startpos
      clist.pop(0) # remove moves
    line = clist
  else: # must be fen then
    print(">>> fen not yet implemented!")    

def go(clist): # pass [timestamp, line, goargs=clist] 
  mytup = board, time.time(), line, clist
  controller(mytup)

commands = { # implemented
		"quit" : quit,
		"uci" : uci,
		"isready" : isready,
		"ucinewgame" : ucinewgame,
		"position" : position,
		"go" : go
} # globals()[cmd](clist) => is undebuggable. Hence a dict

uinput = "empty"

while uinput != "quit": # main UCI loop
  uinput = input() # Sonarqube sees security issue here. Check input.
  clist = uinput.split(" ")
  cmd = clist.pop(0)
  result = commands.get(cmd, "empty")
  if result == "empty":
    print(">>> invalid command")
  else: 
    result(clist)

