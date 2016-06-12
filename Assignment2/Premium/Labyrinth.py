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
		#self.count = 0 # use for haunt function
		self.bridges = []

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
		indicate which corridor the EVIL can block to 
		stop the wizards to reach the exit.
		@return v, if it possible to block return the name's node
		otherwise None
	'''
	def haunt(self):
		def dfs(u, v, pre, low, count): # Apply DFS to find bridges
			count += 1
			pre[v] = count
			low[v] = pre[v]
			for n in self.graph[v].neighbors:
				if pre[n.name] == -1:
					dfs(v, n.name, pre, low, count)
					low[v] = min(low[v], low[n.name])
					if low[n.name] == pre[n.name]:
						self.bridges.append((v, n.name))
				elif n.name != u:
					low[v] = min(low[v], pre[n.name])

		if self.graph[self.exit].neighbors == 1:
			return self.graph[self.exit][0].name
		else:
			low = {n:-1 for n in self.graph}
			pre = {n:-1 for n in self.graph}
			count = 1
			for n in self.graph:
				if pre[n] == -1:
					dfs(n, n, pre, low, count)
			print pre
			print low
			return self.bridges

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