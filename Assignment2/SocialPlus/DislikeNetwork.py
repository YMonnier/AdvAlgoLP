class DislikeNetwork(object):
	'''
		DIRECTED GRAPH
	'''
	def __init__(self):
		self.graph = {}

	'''
		add a node to the graph (person)
		@param name, node's name
	'''
	def add_person(self, name):
		if name not in self.graph:
			self.graph[name] = Node(name)

	'''
		add a edge to the graph (dislike link)
		ie John --> Paul (John doesn't like Paul)
		@param fr, node from
		@param to, node to
	'''
	def dislike(self, fr, to):
		if fr not in self.graph:
			self.add_node(fr)
		if to not in self.graph:
			self.add_node(to)

		self.graph[fr].add_neighbor(self.graph[to])


class Node(object):
	'''
		name: person's name (node's id)
		visited: true if node is visited, otherwise false
		neigbhbors: list of neigbhbors
	'''
	def __init__(self, name):
		self.name = name
		self.visited = False
		self.neighbors = []

	'''
		add a neighbor
		@param neighbor, id of node
	'''
	def add_neighbor(self, neighbor):
		self.neighbors.append(neighbor)