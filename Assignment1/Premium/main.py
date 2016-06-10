from PIL import Image
import Premium

# List of images: 
# Images/orange10x10.png
# Images/green20x20.png
# Images/orange2-10x10
# Images/zelda.png
image = Premium.getImage("Images/orange2-10x10.png")
#corner = (size[0] - cornerSize, size[1] - cornerSize)
#print "corner size:: "+ str(cornerSize) + " | pos:: " + str(corner)

Premium.rabinKarp(image, 4)