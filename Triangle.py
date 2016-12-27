from Shape import Shape
import geometry
from Point import Point
class Triangle(Shape):
	def __init__(self, A, B, C, character):
		self.A = A
		self.B = B
		self.C = C
		self.character = character

	def renderInView(self, view):
		for i in range(0, view.height):
			for j in range(0, view.width):
				if self.pointInTriangle(Point(j,view.height - i - 1)): # previously (j,i)
					view.grid[i][j] = self.character

	def pointInTriangle(self, point):
		areaOfTriangle = geometry.areaOfTriangle(self.A, self.B, self.C)
		totalSubAreas = geometry.areaOfTriangle(point, self.A, self.B) + geometry.areaOfTriangle(point, self.B, self.C) + geometry.areaOfTriangle(point, self.C, self.A)
		if areaOfTriangle == totalSubAreas: return True
		return False
