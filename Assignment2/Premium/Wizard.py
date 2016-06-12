#
# Author Ysee Monnier
# University Of Lodz, Poland
#

from random import randint
from Queue import Queue
import math

class Wizard:
	"""
		name: wizard name
		position: start position (node)
		speed: average per minutes
		time: time to go to the exit
		magical_wand: way to exit the labyrinth
	"""
	def __init__(self, name, position):
		self.name = name
		self.position = position
		self.speed = randint(1, 3)
		self.magical_wand = []
		self.time = 0

	def __str__(self):
		res = "  +| %s, speed: %d\n" % (self.name, self.speed)
		res += "   | magical wand says to go by this way: " + str(self.magical_wand) + "\n"
		res += "   | you will arrive in " + str(self.time) + " minutes\n"
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
			node = Q.get()
			for n in labyrinth[node].neighbors:
				if not labyrinth[n.name].visited:
					labyrinth[n.name].visited = True
					pi[n.name] = node
					Q.put(n.name)
		
		clear_node()

		# Draw the path
		p = exit
		path = [p]
		while p != -1:
			p = pi[p]
			path.insert(0, p)
		self.magical_wand = path[2:]
		self.time = int(math.ceil(float(len(self.magical_wand))/float(self.speed)))
