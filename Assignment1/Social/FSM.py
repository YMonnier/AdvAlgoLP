#
# FSM.py
# String matching with finite automata 
# or Finite State Machine (FSM)
# University Of Lodz, Poland
# String matching
#
import string
import time

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
		#print("Trans lenght...  ::" + str(len(trans)))
		#print("S ::" + str(q))
		q = trans[q][T[i]]
		if q == m:
			#print("OKOK -- " + str(i-m+1))
			shifts.append(i-m+1)
			q = 0
			#shifts.append(i-m+1)

	print("	==> Execution time: %s milliseconds" % ((time.time() - start_time)/1000))
	print("	==> %s matchings" % len(shifts))
	print("	==> shifts " + str(shifts))