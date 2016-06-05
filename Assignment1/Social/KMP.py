#
# KMP.py
# Knuth-Morris-Pratt (KMP)
# Author Ysee Monnier
# University Of Lodz, Poland
# String matching
#

import time

#Table-building
def preprocessing(P):
	m = len(P)
	pi = [0] * m
	k = 0
	for q in range(1,m):
		while k > 0 and P[k] != P[q]:
			k = pi[k]
		if P[k] == P[q]:
			k = k + 1
		pi[q] = k
	return pi


'''
	Knuth-Morris-Pratt Algorithm
	@param T: The search area
	@param P: The candidate to do the search
'''
def KMP(T, P):
	print("*************************************************")
	print("***************** KMP Algorithm *****************")
	print("*************************************************")

	# Start timer
	start_time = time.time()

	# Preprocessing
	pi = preprocessing(P)

	shifts = []
	n = len(T)
	m = len(P)
 	q = 0 # number of characters matched
	for i in range(1, n): # scan the text from left to right
		while q > 0 and T[i] != P[q]:
			q = pi[q] # next character does not match

		if T[i] == P[q]:
			q += 1 # next character matches
		if q == m: # is all of P matched
 			shifts.append(i - (m-1))
			q = 0#pi[q-m] # look for the next match

	print("	==> Execution time: %s seconds" % ((time.time() - start_time)))
	print("	==> %s matchings" % len(shifts))
	#print("	==> %s matchings" % (j-1))	
	#print("	==> shifts " + str(shifts))
