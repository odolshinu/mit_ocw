# 6.00 Problem Set 9
#
# Name:
# Collaborators:
# Time:

import re
from string import *

class Shape(object):
    def area(self):
        raise AttributeException("Subclasses should override this method.")

class Square(Shape):
    def __init__(self, h):
        """
        h: length of side of the square
        """
        self.side = float(h)
    def area(self):
        """
        Returns area of the square
        """
        return self.side**2
    def __str__(self):
        return 'Square with side ' + str(self.side)
    def __eq__(self, other):
        """
        Two squares are equal if they have the same dimension.
        other: object to check for equality
        """
        return type(other) == Square and self.side == other.side

class Circle(Shape):
    def __init__(self, radius):
        """
        radius: radius of the circle
        """
        self.radius = float(radius)
    def area(self):
        """
        Returns approximate area of the circle
        """
        return 3.14159*(self.radius**2)
    def __str__(self):
        return 'Circle with radius ' + str(self.radius)
    def __eq__(self, other):
        """
        Two circles are equal if they have the same radius.
        other: object to check for equality
        """
        return type(other) == Circle and self.radius == other.radius

#
# Problem 1: Create the Triangle class
#
## TO DO: Implement the `Triangle` class, which also extends `Shape`.

class Triangle(Shape):
    def __init__(self,base,height):
        """
	base: base length of triangle
	height: altitude of triangle
	"""
	self.base = float(base)
	self.height = float(height)

    def area(self):
        """
	returns area of the triangle
	"""
	return 0.5 * self.base * self.height

    def __str__(self):
        return 'triangle with base length:' + str(self.base) + ' and height:' + str(self.height)

    def __eq__(self,other):
        """
	Two triangles are equal if they have the same area
	"""
        return type(other) == Triangle and self.area() == other.area()


#
# Problem 2: Create the ShapeSet class
#
## TO DO: Fill in the following code skeleton according to the
##    specifications.

class ShapeSet:
    def __init__(self):
        """
        Initialize any needed variables
        """
	self.item = []
        ## TO DO
    def addShape(self, sh):
        """
        Add shape sh to the set; no two shapes in the set may be
        identical
        sh: shape to be added
        """
	if not len(self.item):
	    self.item.append(sh)
	    return
	else:
	    for i in self.item:
	        if i == sh:
	            print 'already exist'
	            return
	    self.item.append(sh)
        ## TO DO

	

    def __iter__(self):
        """
        Return an iterator that allows you to iterate over the set of
        shapes, one shape at a time
        """
	return self
        ## TO DO

    def next(self):
        for i in self.item:
	    return i

        
    def __str__(self):
        """
        Return the string representation for a set, which consists of
        the string representation of each shape, categorized by type
        (circles, then squares, then triangles)
        """
	for i in self.item:
	    if isinstance(i,Circle):
	        print i.__str__()
	for i in self.item:
	    if isinstance(i,Square):
		print i.__str__()
	for i in self.item:
	    if isinstance(i,Triangle):
		print i.__str__()
        
        ## TO DO
        
#
# Problem 3: Find the largest shapes in a ShapeSet
#
def findLargest(shapes):
    """
    Returns a tuple containing the elements of ShapeSet with the
       largest area.
    shapes: ShapeSet
    """

    temp, maximum = [], 0.0
    for i in shapes.item:
        if i.area() > maximum:
            maximum = i.area()
    for i in shapes.item:
        if i.area() == maximum:
            temp.append(i)
    for i in temp:
        print 'largest shape is %s'%i.__str__()
    ## TO DO

#
# Problem 4: Read shapes from a file into a ShapeSet
#
def readShapesFromFile(filename):
    """
    Retrieves shape information from the given file.
    Creates and returns a ShapeSet with the shapes found.
    filename: string
    """
    a = []
    b = []
    f = open(filename,'r')
    for line in f:
        a = re.findall(r'(\w+),(\S+)', line)
        if a[0][0] == 'circle':
	    obj = Circle(a[0][1])
	    add.addShape(obj)
	elif a[0][0] == 'square':
	    obj = Square(a[0][1])
	    add.addShape(obj)
	else:
	    b = a[0][1].split(',')
	    obj = Triangle(float(b[0]),float( b[1]))
	    add.addShape(obj)
    add.__str__()
    ## TO DO

add = ShapeSet()

def main():
    readShapesFromFile('shapes.txt')
    findLargest(add)

if __name__ == '__main__':
    main()
