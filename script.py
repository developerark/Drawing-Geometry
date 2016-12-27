import os
from View import View
from Rectangle import Rectangle
from Triangle import Triangle
from Line import Line
from Circle import Circle
from Point import Point

def clearScreen():
	os.system('cls' if os.name == 'nt' else 'clear')



view = View(30,30)

while True:
	clearScreen()
	view.drawView()
	print "Shapes Available:"
	print "\t 1. Rectangle"
	print "\t 2. Line"
	print "\t 3. Triangle"
	print "\t 4. Circle"
	print "\t q. Quit"
	input = raw_input("Select Shape>>")
	if input == "Q" or input == "q":
		print "[!] Quiting"
		exit()
	if int(input) == 1 or int(input) == 2 or int(input) == 3 or int(input) == 4:
		if int(input) == 1:
			input = raw_input("Enter Attributes for Rectangle: <xPos yPos width height character> ")
			inputList = input.split(" ")
			rectangle = Rectangle(int(inputList[0]), int(inputList[1]), int(inputList[2]), int(inputList[3]), inputList[4])
			view.addToView(rectangle)
		elif int(input) == 2:
			input = raw_input("Enter Attributes for Line: <x1 y1 x2 y2 character> ")
			inputList = input.split(" ")
			p1 = Point(int(inputList[0]), int(inputList[1]))
			p2 = Point(int(inputList[2]), int(inputList[3]))
			line = Line(p1, p2, inputList[4])
			view.addToView(line)
		elif int(input) == 3:
			input = raw_input("Enter Attributes for Triangle: <x1 y1 x2 y2 x3 y3 character> ")
			inputList = input.split(" ")
			p1 = Point(int(inputList[0]), int(inputList[1]))
			p2 = Point(int(inputList[2]), int(inputList[3]))
			p3 = Point(int(inputList[4]), int(inputList[5]))
			triangle = Triangle(p1, p2, p3, inputList[6])
			view.addToView(triangle)
		elif int(input) == 4:
			input = raw_input("Enter Attributes for Circle: <xPos yPos radius character> ")
			inputList = input.split(" ")
			circle = Circle(Point(int(inputList[0]), int(inputList[1])), int(inputList[2]), inputList[3])
			view.addToView(circle)
	else:
		print "[!] Error: Invalid Input"





