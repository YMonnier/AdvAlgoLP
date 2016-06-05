from PIL import Image

def matchImage(imageName, cornerSize):
	img = Image.open("zelda.png")
	size = img.size # Tuple(width, height)
	print img
	print "image size:: " + str(size)

	pix = img.load() # Pix img	
	corner = (size[0] - cornerSize, size[1] - cornerSize)
	print "corner size:: "+ str(cornerSize) + " | pos:: " + str(corner)