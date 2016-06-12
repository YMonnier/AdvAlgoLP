#
# Author Ysee Monnier
# University Of Lodz, Poland
#

import sys

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

	def add_edge(self, fr, to, distance):
		if fr not in self.graph:
			self.add_node(fr)
		if to not in self.graph:
			self.add_node(to)

		self.graph[fr].add_neighbor(self.graph[to], distance)
		self.graph[to].add_neighbor(self.graph[fr], distance)

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
			res += "Vertex: %s\n Coridors: \n" % v
			for n in self.graph[v].neighbors:
				res += "    | (%s, visited %s, weight %s)\n" % (n.name, n.visited, self.graph[v].get_weight(n))
			res+="\n"
		return res



class Node(object):
	'''
		name, node's id/name 
		visited, true if node is visited, otherwise false
		neigbhbors, list of neigbhbors
	'''
	def __init__(self, name):
		self.name = name
		self.visited = False
		self.distance = sys.maxint # Set distance to infinity
		self.previous = None # No predecessor
		self.neighbors = {}

	def add_neighbor(self, neighbor, distance=0):
		self.neighbors[neighbor] = distance

	def get_weight(self, neighbor):
		return self.neighbors[neighbor]