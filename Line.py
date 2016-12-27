from Shape import Shape
from Point import Point
class Line(Shape):

	def __init__(self, A, B, character):
		self.A = A
		self.B = B
		self.character = character

	def renderInView(self, view):
		for i in range(0, view.height):
			for j in range(0, view.width):
				if self.pointInLine(Point(j, view.height - i - 1)): #previously (j, i)
					view.grid[i][j] = self.character

	def pointInLine(self, point):
		m = (self.B.xCordinate - self.A.xCordinate) / ((self.B.yCordinate - self.A.yCordinate) * 1.0)
		if point.yCordinate == m * point.xCordinate - m * self.A.xCordinate + self.A.yCordinate: return True 
		return False