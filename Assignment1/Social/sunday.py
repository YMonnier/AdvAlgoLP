#
# Sunday.py
# Author Ysee Monnier
# University Of Lodz, Poland
# String matching
#

import time
import string
"""
	Preprocessing sunday
	@param P: Text
"""
def preprocessing(P):
	m = len(P)
	occ = {}
	alphabet = string.ascii_letters + string.punctuation + string.digits + string.whitespace
	# each character of the alphabet 
	for char in alphabet:
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
	print("****************************************************")
	print("***************** Sunday Algorithm *****************")
	print("****************************************************")
	# Start timer
	start_time = time.time()

	#Preprocessing
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

	print("	==> Execution time: %s milliseconds" % ((time.time() - start_time)/1000))
	print("	==> %s matchings" % len(shifts))
	print("	==> shifts " + str(shifts))

