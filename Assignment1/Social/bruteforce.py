#
# bruteforce.py
# Author Ysee Monnier
# University Of Lodz, Poland
# String matching
#

import time

def bruteForce(T, P):
	print("*********************************************************")
	print("***************** Brute Force Algorithm *****************")
	print("*********************************************************")
	# Start timer
	start_time = time.time()

	# Text length
	n = len(T)

	# Pattern length
	m = len(P)

	# Number of occurrences found
	shifts = []

	for i in xrange(0, n - m):
		j = 0
		while j < m and T[i + j] == P[j]:
			j = j + 1
		if j == m:
			shifts.append(i)
	
	print("	==> Execution time: %s milliseconds" % ((time.time() - start_time)/1000))
	print("	==> %s matchings" % len(shifts))
	print("	==> shifts " + str(shifts))