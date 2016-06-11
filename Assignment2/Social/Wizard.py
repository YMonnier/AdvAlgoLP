#
# Author Ysee Monnier
# University Of Lodz, Poland
#

from random import randint
from Queue import Queue

class Wizard:
	"""
		name: wizard name
		position: start position (node)
		speed: average per minutes
	"""
	def __init__(self, name, position):
		self.name = name
		self.position = position
		self.speed = randint(1, 3)
		self.magical_wand = []

	def __str__(self):
		res = "  +| %s, speed: %d\n" % (self.name, self.speed)
		res += "   | magical wand says to go by this way: " + str(self.magical_wand) + "\n"
		return res

	'''
		magical wand allows to help the wizard to 
		find the exit shortest path 
		@param labyrinth, Graph
		@param exit, the exit positon
	'''
	def use_magical_wand(self,labyrinth, exit): 
		def clear_node():
			for n in labyrinth:
				labyrinth[n].visited = False

		pi = {}
		Q = Queue()
		
		# Init
		pi[self.position] = -1 # pi function(predecessor)
		Q.put(self.position)
		labyrinth[self.position].visited = True

		# Breadth First Search Algorithm
		while not Q.empty():
			print Q.queue
			node = Q.get()
			for n in labyrinth[node].neighbors:
				if not labyrinth[n.name].visited:
					labyrinth[n.name].visited = True
					pi[n.name] = node
					Q.put(n.name)
			print Q.queue
		
		clear_node()

		# Draw the path
		p = exit
		path = [p]
		while p != -1:
			p = pi[p]
			path.insert(0, p)
		self.magical_wand = path[1:]

	