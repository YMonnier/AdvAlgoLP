#
# main.py
# Author Ysee Monnier
# String matching
#

import reader
import string
import Bruteforce
import Sunday
import KMP
import FSM
import RabinKarp
#fileName = input('Your txt file: ')
#pattern = input('Your pattern: ')

fileName = 'book.txt'
pattern = 'unapproachable'


print("	==> Pattern :: %s" %pattern)
print("	==> Pattern Length :: %d" %len(pattern))

# Get content's file
s = reader.readFile(fileName)

#Bruteforce Algorithm
Bruteforce.bruteForce(s, pattern)

#Sunday Algorithm
Sunday.sunday(s, pattern)

#KMP Algorithm
KMP.KMP(s, pattern)

#FSM Algorithm
FSM.FSM(s, pattern)

#Rabin-Karp Algorithm
RabinKarp.rabinKarp(s, pattern)