#
# Author Ysee Monnier
# University Of Lodz, Poland
#

from Labyrinth import Labyrinth
from Wizard import Wizard

labyrinth = Labyrinth()

# 1 - Add nodes
labyrinth.add_node('A')
labyrinth.add_node('B')
labyrinth.add_node('C')
labyrinth.add_node('D')
labyrinth.add_node('E')
labyrinth.add_node('F')
labyrinth.add_node('G')
labyrinth.add_node('H')
labyrinth.add_node('I')
labyrinth.add_node('I')
labyrinth.add_node('J')
labyrinth.add_node('Y')


# 2 - Add edges
labyrinth.add_edge('A', 'B', 5)
labyrinth.add_edge('A', 'C', 10)
labyrinth.add_edge('B', 'C', 15)

labyrinth.add_edge('Y', 'C', 20)

labyrinth.add_edge('Y', 'D', 20)
labyrinth.add_edge('E', 'D', 10)
labyrinth.add_edge('H', 'D', 5)
labyrinth.add_edge('H', 'E', 5)
labyrinth.add_edge('H', 'F', 10)

labyrinth.add_edge('Y', 'J', 20)
labyrinth.add_edge('J', 'I', 30)
labyrinth.add_edge('G', 'I', 5)

# 3 - Set the labyrinth exit
labyrinth.set_exit_point('G')

# 4 - Add wizards
#labyrinth.add_wizard(Wizard('Harry Potter', 'G'))
labyrinth.add_wizard(Wizard('Ron Weasley', 'C'))
labyrinth.add_wizard(Wizard('Draco Malfoy', 'E'))

# 5 - Haunted the Labyrinth
evilPlan = labyrinth.haunt()


# Engine printing

game = "---------------------------\n"
game += "------ THE LABYRINTH ------\n"
game += "---------------------------\n\n"

wizards = labyrinth.wizards
game_time = max(w.time for w in wizards)

for minute in xrange(1, game_time + 1):
	game += "+| minute %d\n" % minute
	for w in wizards:
		if minute < w.time:
			game += "    +| %s\n" % w.name
			game += "     | " + str(w.magical_wand[((minute-1) * w.speed):(minute * w.speed)]) + "\n"
		elif minute == w.time: 
			game += "    +| %s\n" % w.name
			game += "     | " + str(w.magical_wand[((minute-1) * w.speed):(minute * w.speed)]) + " ARRIVED\n"


min_time = min(w.time for w in wizards)
winners = filter(lambda w: w.time == min_time, wizards)

if len(winners) > 1:
	game += "\n  -------- WINNERS --------  \n"
	game += "    " + str(map(lambda w: w.name, winners))
else:
	game += "\n  -------- WINNER --------  \n"
	game += "    " + str(winners[0].name)

evil = "\n---------------------------\n"
evil += "------ THE EVIL PLAN ------\n"
evil += "---------------------------\n\n"

if len(evilPlan) == 0:
	evil += "Lord Waldemar is too bad..."
else:
	evil += "Lord Waldemar can block: \n"
	for b in evilPlan:
		for w in evilPlan[b]:
			evil += "     |  %s\n" % map(lambda w: w.name,labyrinth.get_wizard(w))

		evil += "       at position %s\n\n" % b

print labyrinth
#print game
print evil