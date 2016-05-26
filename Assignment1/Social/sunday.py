#
# sunday.py
# Author Ysee Monnier
# String matching
#

import reader
import string
import time

"""
	Preprocessing sunday
	@param P: Text
"""
def preprocessing(P):
	m = len(P)
	occ = {}
	# each character of the alphabet 
	for char in string.printable:
		occ[char] = -1

	for i in range(m): 
		char = P[i]
		occ[char] = i

	return occ

"""
	Check pattern matches with text at specific index
	@param T: Text
	@param P: Pattern
	@param i: Index from text
"""
def isInP(T, P, i):
	for char in P:
		if char != T[i]:
			return False
		i += 1

	return True

"""
	Sunday Algorithm
"""
def sunday(T, P):
	occ = preprocessing(P)

	i = 0
	shifts = []
	n = len(T)
	m = len(P)
	occ = preprocessing(P)

	for i in range(n - m + 1):
		if isInP(T, P, i):
			shifts.append(i)
		i += m
		if i < n:
			i -= occ[T[i]]

	return shifts

#fileName = input('Your txt file: ')
#pattern = input('Your pattern: ')

fileName = 'book.txt'
pattern = 'of'

# Get content's file
s = reader.readFile(fileName)

# Start timer
start_time = time.time()

#Bruteforce
shifts = sunday(s, pattern)

print("Execution time: %s seconds" % (time.time() - start_time))
print("%s matchings" % len(shifts))
print("shifts " + str(shifts))
