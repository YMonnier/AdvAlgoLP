#
# bruteforce.py
# Author Ysee Monnier
#

import reader
import string
import time

#fileName = input('Your txt file: ')
#pattern = input('Your pattern: ')

fileName = 'book.txt'
pattern = 'from the window or the door'

# Get content's file
s = reader.readFile(fileName)

# Start timer
start_time = time.time()

n = len(s)
m = len(pattern)

# Number of occurrences found
res = 0

# Brute force algorithm
for i in xrange(0, n - m):
	j = 0
	while j < m and s[i + j] == pattern[j]:
		j = j + 1
	if j == m:
		res = res + 1

print("--- %s seconds ---" % (time.time() - start_time))
print res


