#
# FSM.py
# String matching with finite automata 
# or Finite State Machine (FSM)
# University Of Lodz, Poland
# String matching
#
import string
import time

'''
	Build a two-dimentional array which reprensent the Finite Automata
'''
def computeTransition(P):
	m = len(P)
	alphabet = string.ascii_letters + string.punctuation + string.digits + string.whitespace
	trans = [{c:0 for c in alphabet} for i in range(m)]
	for q in range(m):
		for c in alphabet:
			k = min(m, q+1)
			while P[:k] != (P[:q]+c)[-k:]:
				k-=1
			trans[q][c]=k
	return trans


'''
	Finite State Machine Algorithm
	@param T: The search area
	@param P: The candidate to do the search
'''
def FSM(T, P):
	print("*************************************************")
	print("***************** FSM Algorithm *****************")
	print("*************************************************")

	# Start timer
	start_time = time.time()

	#Preprocessing
	trans = computeTransition(P)
	shifts = []
	m = len(P)
	n = len(T)
	q = 0
	for i in range(0, n):
		q = trans[q][T[i]]
		if q == m:			
			shifts.append(i-m+1)
			q = 0

	print("	==> Execution time: %s seconds" % ((time.time() - start_time)))
	print("	==> %s matchings" % len(shifts))
	#print("	==> shifts " + str(shifts))