class Shape:
	def __init__(self):
		self.xPos = None
		self.yPos = None

	def renderInView(self, view):
		print "Super RenderInView: No rendering logic defined. Every subtype of shape may have its own rendering logic. Override this method in its own class."
