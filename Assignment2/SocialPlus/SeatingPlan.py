from DislikeNetwork import DislikeNetwork

def createPlan(graph):

	'''
		Add a person to a table
		if is not possible, we get out this person
		@person, person want to add_person
		@tables, tables to add person
	'''
	def add_person(person, tables):
		if person not in tables[0]:
			tables[0].append(person)
		elif person not in tables[1]:
			tables[1].append(person)
		else: tables[2].append(person)


	# Init
	
	# Table of table (Table1, Table2, GetOut)
	tables = ([], [], [])

	# pi table (predecessor)
	pi = {}

	# Depth First Algorithm	
	for person in graph:

		if not graph[person].visited:
			stack = []
			stack.append(person)
			add_person(person, tables)
			pi[person] = -1
			while stack != []:
				dislike

	return 0


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

	table = createPlan(network.graph)