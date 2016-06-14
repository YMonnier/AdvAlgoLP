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
import gc
#fileName = input('Your txt file: ')
#pattern = input('Your pattern: ')

gc.disable() 

fileName = 'book.txt'

#reader.readFile("Paragraphs/para0.txt")
#reader.readFile("Paragraphs/para1.txt") 
#reader.readFile("Paragraphs/para2.txt") 
#"of"
#pattern = reader.readFile("Paragraphs/para2.txt")
pattern = "his"
# Get content's file
s = reader.readFile(fileName)

#print("	==> Text :: %s" %s)
print("	==> Pattern :: %s" %pattern)
print("	==> Pattern Length :: %d" %len(pattern))

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
