from DislikeNetwork import DislikeNetwork

def createPlan(graph):

	'''
		Check if dislike persons are already seated 
		@param dislike_persons: list of dislike persons
		@table: list of person already seated
		@return True if dislike persons are in the table,
		otherwise False
	'''
	def contains(dislike_persons, table):
		for i in dislike_persons:
			for j in table:
				if i == j:
					return True
		return False
	
	'''
		Add a person to a table
		if is not possible, we get out this person
		@param person: person we want to add
		@param dislike_persons: list of dislike persons
		@param tables, tables to add person
	'''
	def add_person(person, dislike_persons, tables):
		if not contains(dislike_persons, tables[0]):
			tables[0].append(person)
		elif not contains(dislike_persons, tables[1]):
			tables[1].append(person)
		else: tables[2].append(person)


	# Init
	
	# Table of table (Table1, Table2, GetOut)
	tables = ([], [], [])

	# pi table (list of predecessor)
	pi = {n:[] for n in graph}

	# Depth First Algorithm for each node,	
	for person in graph: # because, some nodes can be not connected
		if not graph[person].visited:
			stack = []
			stack.append(person)
			pi[person].append(person)
			
			while stack != []:
				dislike_p = stack.pop()
				if not graph[dislike_p].visited:
					graph[dislike_p].visited = True
					add_person(dislike_p, pi[dislike_p], tables)
					for n in graph[dislike_p].neighbors:
						pi[n.name].append(dislike_p)
						stack.append(n.name)
					

	#print "Predecessor"
	#for key, value in pi.iteritems():
	#	print str(key) + " - " + str(value)

	return tables

if __name__ == '__main__':

	network = DislikeNetwork()

	network.add_person('Michel')
	network.add_person('Yann')
	network.add_person('Georges')
	network.add_person('Veronique')
	network.add_person('Jose')
	network.add_person('Peter')

	network.dislike('Michel', 'Veronique')
	network.dislike('Veronique', 'Michel')
	network.dislike('Georges', 'Veronique')
	network.dislike('Georges', 'Yann')
	network.dislike('Yann', 'Peter')
	network.dislike('Peter', 'Michel')
	network.dislike('Jose', 'Georges')

	print network
	tables = createPlan(network.graph)
	
	#Print tables
	maxTab = max(map(lambda t: len(t), tables))
	res = "|-----------------|-----------------|-----------------|\n"
	res += "|     Table 1     |     Table 2     |     Get Out     |\n"
	res += "|-----------------|-----------------|-----------------|\n"
	for i in range(maxTab):
		t1 = "%s" % tables[0][i] if i < len(tables[0]) else ''
		t2 = "%s" % tables[1][i] if i < len(tables[1]) else ''
		t3 = "%s" % tables[2][i] if i < len(tables[2]) else ''
		res += "| " + str(t1).ljust(16) + "| " + str(t2).ljust(16) + "| " + str(t3).ljust(16) + "|\n"
	print res