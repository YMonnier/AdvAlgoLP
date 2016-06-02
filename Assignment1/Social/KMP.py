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
	occ = [0] * m
	a = 0
	for i in xrange(1, m):
		while a > 0 and P[a] != P[i]:
			a = occ[a - 1]
		if P[a] == P[i]:
			a = a + 1
		occ[i] = a
	return occ

def KMP(T, P):
	print("*************************************************")
	print("***************** KMP Algorithm *****************")
	print("*************************************************")

	# Start timer
	start_time = time.time()

	#Preprocessing
	occ = preprocessing(P)
	shifts = []
	n = len(T)
	m = len(P)
 	j = 0
	for i in range(n):
		while j > 0 and T[i] != P[j]:
			j = occ[j - 1]
		if T[i] == P[j]:
			j += 1
		if j == m:
 		#shifts.append(i - m + 1)
			break


	print("	==> Execution time: %s milliseconds" % ((time.time() - start_time)/1000))
	#print("	==> %s matchings" % len(shifts))
	print("	==> %s matchings" % (j-1))	
	#print("	==> shifts " + str(shifts))
