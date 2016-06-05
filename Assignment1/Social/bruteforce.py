#
# Bruteforce.py
# Author Ysee Monnier
# University Of Lodz, Poland
# String matching
#

import time


'''
	Brute-Force Algorithm
	@param T: The search area
	@param P: The candidate to do the search
'''
def bruteForce(T, P):
	print("*************************************************")
	print("************* Brute Force Algorithm *************")
	print("*************************************************")

	# Start timer
	start_time = time.time()

	# Text length
	n = len(T)

	# Pattern length
	m = len(P)

	# Number of occurrences found
	shifts = []

	for i in xrange(0, n - (m-1)):
		j = 0
		while j < m and T[i + j] == P[j]:
			j = j + 1
		if j == m:
			shifts.append(i)
	
	print("	==> Execution time: %s seconds" % ((time.time() - start_time)))
	print("	==> %s matchings" % len(shifts))
	#print("	==> shifts " + str(shifts))