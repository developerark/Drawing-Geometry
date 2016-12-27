class View:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.queue = []
		self.grid = []
		for i in range(0, height):
			row = []
			for j in range(0, width):
				row.append("*")
			self.grid.append(row)

	def addToView(self, element):
		self.queue.append(element)
		self.renderShapesInView()

	def renderShapesInView(self):
		# think of element as Shape objects now
		for element in self.queue:
			element.renderInView(self)

	def drawView(self):
		for i in range(0, self.height):
			for j in range(0, self.width):
				print self.grid[i][j],
			print

