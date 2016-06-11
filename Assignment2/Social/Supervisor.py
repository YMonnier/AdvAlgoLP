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
labyrinth.add_edge('A', 'B')
labyrinth.add_edge('C', 'B')
labyrinth.add_edge('D', 'B')
labyrinth.add_edge('D', 'E')
labyrinth.add_edge('E', 'C')
labyrinth.add_edge('D', 'F')
labyrinth.add_edge('E', 'F')

# Set the labyrinth exit
labyrinth.set_exit_point('F')

labyrinth.add_wizard(Wizard('Harry Potter', 'A'))
labyrinth.add_wizard(Wizard('Lord Voldemort', 'C'))

print labyrinth