#
# main.py
# Author Ysee Monnier
# String matching
#

import reader
import string
import bruteforce
import sunday
import KMP
import FSM
#fileName = input('Your txt file: ')
#pattern = input('Your pattern: ')

fileName = 'book.txt'
pattern = 'cheetah'


print("	==> Pattern :: %s" %pattern)

# Get content's file
s = reader.readFile(fileName)

#Bruteforce Algorithm
bruteforce.bruteForce(s, pattern)

#Sunday Algorithm
sunday.sunday(s, pattern)

#KMP Algorithm
KMP.KMP(s, pattern)

#FSM Algorithm
FSM.FSM(s, pattern)