from Point import Point

def areaOfTriangle(A, B, C):
	return  abs((((A.xCordinate*(B.yCordinate-C.yCordinate)) +(B.xCordinate*(C.yCordinate-A.yCordinate)) +(C.xCordinate*(A.yCordinate-B.yCordinate)))/2.0))
