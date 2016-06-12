#
# Author Ysee Monnier
# University Of Lodz, Poland
#

from PIL import Image

'''
	Open an image with a specific name. ('zelda.png')
	@param imageName
	@return image
'''
def getImage(imageName):
	return Image.open(imageName)

def rgbCompare(rgb1, rgb2):
	return rgb1[0] == rgb2[0] and rgb1[1] == rgb2[1] and rgb1[2] == rgb2[2]

'''
	return encoded color
	@param pixel, tuple(R,G,B,A)
	@return encoded color
'''
def getPixel(pixel):
	return pixel[0] << 24 | pixel[1] << 16 | pixel[2] << 8 | pixel[3]

'''
	Brute-Force Algothm applied
	when hash_c == hash_K
	return m, number of occurence found.
'''
def bruteForce(pic, x, y, K, cornerX):
	m = 0
	for yy in range(K):
		for xx in range(K):
			if pic[x+xx, y + yy] == pic[cornerX + xx, yy]:
				m += 1
	return m

'''
	Hash a pixel column
	@pic, picture
	@param x, x start coordinate 
	@param y, y start coordinate
	@param K, column length
	@param DH, value for double hash
'''
def hash(pic, x, y, K, DH):
	h = 0
	for yi in range(K):
		h += (getPixel(pic[x,y + yi]) * K**(yi + DH - 1)) % 3
	return h

'''
	@param image, Picture
	@param K, Corner of the picture. Pattern we want 
	to find into the picture
'''
def rabinKarp(image, K):
	print("*************************************************")
	print("***************** Premium Part ******************")
	print("*************************************************")
	imgSize = image.size
	width = imgSize[0]
	height =  imgSize[1]
	cornerX = (width - K)
	print "Image size: " + str(imgSize)
	print "Corner: " + str(K)

	#Check given corner
	if K > imgSize[0] or K > imgSize[1]:
		print "Error: given corner is too high"
		return

	# Get 2-dimensional array of image's pixel
	# imgPix[x,y] -> pixel
	imgPix = image.load()

	print "------\n"

	# Preprocessing	
	# top-rigth corner Hash with size K
	hash_k = 0

	#occurence's index found
	shifts = []

	spiriousHits = 0

	for x in range(K): # Hash corner
		hash_k += hash(imgPix, cornerX + x, 0, K, K - x)

	for y in range(height - K + 1): # for each row
		hash_p = 0 # Current hash (picture hash)
		for x in range(K): # Hash current image 0 to K size
			hash_p += hash(imgPix, x, y, K, K - x)

		for x in xrange(width - K + 1): # for each column
			if hash_p == hash_k: # Same hash code
				if bruteForce(imgPix, x, y, K, cornerX) == K**2: # apply brute-force
					shifts.append((x, y))
				else:
					spiriousHits += 1
			if x < (width - K) and y < (height - K):
				hash_p = hash_p - hash(imgPix, x, y, K, K) # remove first column
				hash_p = hash_p + hash(imgPix, x + K, y, K, 1) # add next column

	print("	==> %s matchings" % len(shifts))
	print("	==> shifts " + str(shifts))	
	print("	==> spirous hits " + str(spiriousHits))	