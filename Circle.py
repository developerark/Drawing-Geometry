from Shape import Shape
from Point import Point

class Circle(Shape):
	def __init__(self, center, radius, character):
		self.center = center
		self.radius = radius
		self.character = character

	def renderInView(self, view):
		for i in range(0, view.height):
			for j in range(0, view.width):
				if self.pointInCircle(Point(j,view.height - i - 1)): # previously (j,i)
					view.grid[i][j] = self.character

	def pointInCircle(self, point):
		distance = ((self.center.xCordinate - point.xCordinate)**2 + (self.center.yCordinate - point.yCordinate)**2)**0.5
		if distance <= self.radius: return True
		return False