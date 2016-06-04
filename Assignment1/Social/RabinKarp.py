#
# RabinKarp.py
# Version of Rabin-Karp
# University Of Lodz, Poland
# String matching
#

import time

def rabinKarp(T, P):
	print("*************************************************")
	print("************* Rabin-Karp Algorithm **************")
	print("*************************************************")

	# Start timer
	start_time = time.time()

	n = len(T)
	m = len(P)
	d = 256
	q = 11
	h = pow(d,m-1)%q
	p = 0
	t = 0
	shifts = []
	for i in range(m): # preprocessing
		p = (d * p + ord(P[i])) % q
		t = (d * t + ord(T[i])) % q
	for s in range(n - m + 1): # matching
		if p == t:
			match = True
			for i in range(m):
				if P[i] != T[s + i]:
					match = False
					break
			if match:
				shifts.append(s)
		if s < n-m:
			t = (t - h * ord(T[s])) % q
			t = (t * d + ord(T[s + m])) % q
			t = (t + q) % q
	
	print("	==> Execution time: %s seconds" % ((time.time() - start_time)))
	print("	==> %s matchings" % len(shifts))
	#print("	==> shifts " + str(shifts))