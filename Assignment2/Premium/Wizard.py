#
# Author Ysee Monnier
# University Of Lodz, Poland
#

from random import randint
import heapq
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
		res = "  +| %s, speed: %d, position: %s\n" % (self.name, self.speed, self.position)
		res += "   | magical wand says to go by this way: " + str(self.magical_wand) + "\n"
		res += "   | you will arrive in " + str(self.time) + " minutes\n"
		return res

	'''
		magical wand allows to help the wizard to 
		find the exit shortest path 
		@param labyrinth, Graph
		@param exit, the exit positon
	'''
	def use_magical_wand(self, labyrinth, exit): 
		def shortest(v, path):
			if v.previous and v.previous.distance != 0:
				path.append(v.previous.name)
				shortest(v.previous, path)

		def dijkstra(graph, start, target):
			start.distance = 0

			#queue = [v for v in graph]
			queue = [(graph[v].distance, v) for v in graph]
			heapq.heapify(queue)
			#heapq.heapify(queue)

			while len(queue):
				v = heapq.heappop(queue)
				current = graph[v[1]]
				current.visited = True

				for n in current.neighbors:
					if n.visited: # if visited, skip
						continue
					new_dist = current.distance + current.get_weight(n)
					
					if new_dist < n.distance:
						n.distance = new_dist
						n.previous = current


				# Rebuild the queue with unvisited nodes
				queue = [(graph[v].distance, v) for v in graph if not graph[v].visited]
				heapq.heapify(queue)

		# Exec
		start = labyrinth[self.position]
		target = labyrinth[exit]

		dijkstra(labyrinth, start, target) 

		#Path
		path = [target.name]
		shortest(target, path)

		self.magical_wand = path[::-1]
		self.time = int(math.ceil(float(len(self.magical_wand))/float(self.speed)))

		