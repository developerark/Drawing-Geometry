import Shape
from Shape import Shape

class Rectangle(Shape):
	def __init__(self, xPos, yPos, width, height, character):
		Shape.__init__(self)
		self.xPos = xPos     #inherited and allocated from superclass but initialized here
		self.yPos = yPos 	 #inherited and allocated from superclass but initialized here
		self.width = width
		self.height = height
		self.character = character

	def renderInView(self, view):
		for i in range(0, view.height):
		 	for j in range(0, view.width):
		 		if self.pointInRectangle(j, view.height - i - 1): # previously (j,i)
		 			view.grid[i][j] = self.character

	def pointInRectangle(self, x, y):
		if x >= self.xPos and x<self.xPos +self.width and y>=self.yPos and y<=self.yPos + self.height: return True
		return False



