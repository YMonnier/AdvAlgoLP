#
# book.py
# Author Ysee Monnier
#

# Read file and return all content to string.
def readFile(fileName):
	file = open(fileName, 'r')
	return file.read()