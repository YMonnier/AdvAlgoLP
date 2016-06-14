#
# Author Ysee Monnier
# University Of Lodz, Poland
#

import sys
from Queue import Queue

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

		# Undirected
		self.graph[fr].add_neighbor(self.graph[to], distance)
		self.graph[to].add_neighbor(self.graph[fr], distance)

	'''
		Add a wizard to the labyrinth
		@param wizard, wizard object
	'''
	def add_wizard(self, wizard):
		if wizard not in self.wizards:
			self.wizards.append(wizard)
			wizard.use_magical_wand(self.graph, self.exit)
			self.clear_nodes()

	'''
		get list of wizards with a specific position
	'''
	def get_wizard(self, position):
		return filter(lambda w: w.position == position, self.wizards)

	'''
		Define exit point into the labyrinth
		@param position, exit position
	'''
	def set_exit_point(self, position):
		self.exit = position

	'''
		Re-initialize all node
	'''
	def clear_nodes(self):
		for n in self.graph:
				self.graph[n].visited = False
				self.graph[n].distance = sys.maxint # Set distance to infinity
				self.graph[n].previous = None # No predecessor

	'''
		indicate which corridor the EVIL can block to 
		stop the wizards to reach the exit.
		@return evilPlan, The Evil plan
	'''
	def haunt(self):
		'''
			Apply DFS to find bridges on the current graph
			@param u, previous node
			@param v, node we want to visite
			@param pre, order in which dfs examines v (discovery times of visited vertices)
			@param low, lowest preorder
			@param count, discovery time
			@param res, list of bridges discovered(tuple from,to)
		'''
		def dfs(u, v, pre, low, count, res): # Apply DFS to find bridges
			count += 1
			pre[v] = count
			low[v] = pre[v]
			for n in self.graph[v].neighbors:
				if pre[n.name] == -1:
					dfs(v, n.name, pre, low, count, res)
					low[v] = min(low[v], low[n.name])
					if low[n.name] == pre[n.name]:
						print 'TUPLE (%s, %s)' % (v, n.name)
						res.append((v, n.name))
				elif n.name != u:
					low[v] = min(low[v], pre[n.name])

		'''
			Apply bfs to current graph to find
			if on this sub-graph there 
			are wizards or exit point
			@param source, start point
			@param exception, skip the exception node
			@param wizardsPos, wizards position.
		'''
		def bfs(source, exception, wizardsPos):
			res = []
			queue = Queue()
			self.graph[source].visited = True # Mark visited
			queue.put(source) # add to Queue
			while not queue.empty():
				node = queue.get() #pop
				if node in wizardsPos or node == self.exit:
					res.append(node)
				for n in self.graph[node].neighbors:
					if not n.visited and n.name != exception:
						n.visited = True
						queue.put(n.name)
			return res


		# Find bridges
		low = {n:-1 for n in self.graph}
		pre = {n:-1 for n in self.graph}
		bridges = []
		count = 0
		for n in self.graph:
			if pre[n] == -1:
				dfs(n, n, pre, low, count, bridges)


		# Find wich bridge the EVIL can block
		evilPlan = {} # block: wizards
		wizardsPos = [w.position for w in self.wizards]

		for bridge in bridges: # couple[(from, to)]
			left = bfs(bridge[0],bridge[1], wizardsPos)
			right = bfs(bridge[1],bridge[0], wizardsPos)
			self.clear_nodes()

			if self.exit in left and len(right) != 0:
				if bridge[1] == self.exit:
					evilPlan[bridge[0]] = right
				else: 
					evilPlan[bridge[1]] = right

				evilPlan[bridge[0]] = right
			elif self.exit in right and len(left) != 0:
				if bridge[1] == self.exit:
					evilPlan[bridge[0]] = left
				else: 
					evilPlan[bridge[1]] = left
		return evilPlan

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
		previous, node's predecessor
		distance, node's distance
	'''
	def __init__(self, name):
		self.name = name
		self.visited = False
		self.distance = sys.maxint # Set distance to infinity
		self.previous = None # No predecessor
		self.neighbors = {}

	def __str__(self):
		return 'name %s, vis %s, dis %s, pre %s' % (self.name, self.visited, self.distance, self.previous)

	'''
		add a neigbhbor to the current node
		@param neighbor, name's node
		@param distance, weight/distance
	'''
	def add_neighbor(self, neighbor, distance=0):
		self.neighbors[neighbor] = distance


	def get_weight(self, neighbor):
		return self.neighbors[neighbor]