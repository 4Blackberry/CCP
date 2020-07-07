"""
  Inspired by code of Mark VandeWettering.
    https://brainwagon.org/2015/07/09/one-dimensional-cellular-automata-code-in-python/
  
  Written by Ties van Essen and Sofie Van den Braembussche.

  Cellular Automaton, n = 2, totalistic.
"""

import sys
import random
from colorama import Fore

width = 49
time = 30
neighbourhood = 3
# rule is in the range [0, 2**(neighbourhood + 1]
rule = 5

w = width * [0]
nw = width * [0]

for i in range(width):
  w[i] = random.randint(0, 1)

# rtab is space for the rule table.  It maps all
# numbers from [0, 2**neighbourhood] to either a 0 or 1.
# So if neighbourhood = 3, rtab = [0, 0, 0, 0, 0, 0, 0, 0].
rtab = (neighbourhood + 1) * [0] # neighbourhood + 1 -> 0 - neighbourhood

# code takes the rule in binary, and turns it around.
for i in range(neighbourhood + 1):
    if ((2**i) & rule) != 0:
        rtab[i] = 1

# Potentially change this to coloured squares.
# It is the lattice.
def lattice(r):
    for x in r:
        if x == 1:
            sys.stdout.write(Fore.BLACK + u"\u2588")
        else:
            sys.stdout.write(Fore.WHITE + u"\u2588")
    sys.stdout.write('\n')

# And this is the time.
for t in range(time):
    lattice(w)
    for x in range(width):
        sum = 0
        for d in range(neighbourhood):
            sum = sum + w[(x + d + width - int(neighbourhood/2)) % width] # f.e: 0, 1, 0 -> sum = 1
        nw[x] = rtab[sum]
    w, nw = nw, w
