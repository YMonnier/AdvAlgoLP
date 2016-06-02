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

#fileName = input('Your txt file: ')
#pattern = input('Your pattern: ')

fileName = 'book.txt'
pattern = 'cheetah'


print("	==> Pattern :: %s" %pattern)

# Get content's file
s = reader.readFile(fileName)

#Bruteforce
bruteforce.bruteForce(s, pattern)

#Sunday
sunday.sunday(s, pattern)

#KMP
KMP.KMP(s, pattern)