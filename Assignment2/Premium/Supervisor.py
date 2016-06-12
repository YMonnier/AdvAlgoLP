#
# Author Ysee Monnier
# University Of Lodz, Poland
#

from Labyrinth import Labyrinth
from Wizard import Wizard

labyrinth = Labyrinth()

# Add nodes
labyrinth.add_node('A')
labyrinth.add_node('B')
labyrinth.add_node('C')
labyrinth.add_node('D')
labyrinth.add_node('E')
labyrinth.add_node('F')

# Add edges
labyrinth.add_edge('A', 'B', 20)
labyrinth.add_edge('C', 'B', 5)
labyrinth.add_edge('D', 'B', 10)
labyrinth.add_edge('D', 'E', 10)
labyrinth.add_edge('E', 'C', 10)
labyrinth.add_edge('D', 'F', 30)
labyrinth.add_edge('E', 'F', 10)

# Set the labyrinth exit
labyrinth.set_exit_point('F')

labyrinth.add_wizard(Wizard('Harry Potter', 'A'))
labyrinth.add_wizard(Wizard('Lord Voldemort', 'C'))

print labyrinth


# Engine

res = "---------------------------\n"
res += "------ THE LABYRINTH ------\n"
res += "---------------------------\n\n"

wizards = labyrinth.wizards
game_time = max(w.time for w in wizards)

for minute in xrange(1, game_time + 1):
	res += "+| minute %d\n" % minute
	for w in wizards:
		if minute < w.time:
			res += "    +| %s\n" % w.name
			res += "     | " + str(w.magical_wand[((minute-1) * w.speed):(minute * w.speed)]) + "\n"
		elif minute == w.time: 
			res += "    +| %s\n" % w.name
			res += "     | " + str(w.magical_wand[((minute-1) * w.speed):(minute * w.speed)]) + " ARRIVED\n"


min_time = min(w.time for w in wizards)
winners = filter(lambda w: w.time == min_time, wizards)

if len(winners) > 1:
	res += "\n  -------- WINNERS --------  \n"
	res += "    " + str(map(lambda w: w.name, winners))
else:
	res += "\n  -------- WINNER --------  \n"
	res += "    " + str(winners[0].name)

print res