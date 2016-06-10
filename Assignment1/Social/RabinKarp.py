#
# RabinKarp.py
# Version of Rabin-Karp
# University Of Lodz, Poland
# String matching
#

import time

'''
	Rabin-Karp Algorithm
	@param T: The search area
	@param P: The candidate to do the search
'''
def rabinKarp(T, P):
	print("*************************************************")
	print("************* Rabin-Karp Algorithm **************")
	print("*************************************************")

	# Start timer
	start_time = time.time()

	n = len(T)
	m = len(P)
	d = 257
	q = 101
	h = pow(d,m-1)%q
	hash_p = 0
	hash_t = 0
	shifts = []
	for i in range(m): # preprocessing (hash)
		hash_p = (d * hash_p + ord(P[i])) % q
		hash_t = (d * hash_t + ord(T[i])) % q
	for s in range(n - m + 1): # matching
		if hash_p == hash_t: # if match
			match = True
			for i in range(m):
				if P[i] != T[s + i]:
					match = False
					break
			if match:
				shifts.append(s)
		if s < n-m: # substract first text letter hash and add last hash letter
			hash_t = (hash_t - h * ord(T[s])) % q
			hash_t = (hash_t * d + ord(T[s + m])) % q
			hash_t = (hash_t + q) % q
	print("	==> Execution time: %s seconds" % ((time.time() - start_time)))
	print("	==> %s matchings" % len(shifts))
	#print("	==> shifts " + str(shifts))	