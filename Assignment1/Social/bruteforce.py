#
# bruteforce.py
# Author Ysee Monnier
# String matching
#

import reader
import string
import time

def bruteForce(T, P):
	# Text length
	n = len(T)

	# Pattern length
	m = len(P)

	# Number of occurrences found
	res = []

	for i in xrange(0, n - m):
		j = 0
		while j < m and s[i + j] == pattern[j]:
			j = j + 1
		if j == m:
			res.append(i)
	return res


#fileName = input('Your txt file: ')
#pattern = input('Your pattern: ')

fileName = 'book.txt'
pattern = 'of'

# Get content's file
s = reader.readFile(fileName)

# Start timer
start_time = time.time()

#Bruteforce
shifts = bruteForce(s, pattern)

print("Execution time: %s seconds" % (time.time() - start_time))
print("%s matchings" % len(shifts))
print("shifts " + str(shifts))