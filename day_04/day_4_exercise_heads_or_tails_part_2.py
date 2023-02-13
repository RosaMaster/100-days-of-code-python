import sys
import os
import random

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

x = int(0)
y = int(1)
test = random.randint(x,y)

#x = random.randrange(1,52)
if test == 0:
  print("Heads")
else:
  print("Tails")

#restart_program()