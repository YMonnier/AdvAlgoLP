#
# Author Ysee Monnier
# University Of Lodz, Poland
#
# graph data struct: http://www.bogotobogo.com/python/python_graph_data_structures.php
# Python Patterns: https://www.python.org/doc/essays/graphs/

class Labyrinth(object):
	"""
		UNDIRECTED GRAPH
		graph: labyrinth
		exit: the exit point
		wizards: list of wizards
	"""

	def __init__(self):
		self.graph = {}
		self.exit = ''
		self.wizards = []

	def __iter__(self):
		return iter(self.graph.values())

	def add_node(self, node):
		if node not in self.graph:
			self.graph[node] = Node(node)

	def add_edge(self, fr, to):
		if fr not in self.graph:
			self.add_node(fr)
		if to not in self.graph:
			self.add_node(to)

		self.graph[fr].add_neighbor(self.graph[to])
		self.graph[to].add_neighbor(self.graph[fr])

	def add_wizard(self, wizard):
		if wizard not in self.wizards:
			self.wizards.append(wizard)
			wizard.use_magical_wand(self.graph, self.exit)

	def set_exit_point(self, position):
		self.exit = position

	'''
		Print each nodes with their neigbhbors
	'''
	def __str__(self):
		res = "Wizards\n---------\n"
		for w in self.wizards:
			res += str(w)

		res += "\nLabyrinth\n---------\n"
		for v in self.graph:
			res += "Vertex: " + str(v) + "\n Coridors: \n "
			for n in self.graph[v].neighbors:
				res += "(" + str(n.name) + ", visited " + str(n.visited) + ") | "
			res+="\n"
		return res



class Node(object):
	'''
		name, node's id/name 
		visited, true if node is visited, otherwise false
		neigbhbors, list of neigbhbors
	'''
	def __init__(self, name,):
		self.name = name
		self.visited = False
		self.neighbors = []

	def add_neighbor(self, neighbor):
		self.neighbors.append(neighbor)