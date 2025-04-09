# Define Rectangle class
class Rectangle(object):

    #initializer
    def __init__(self, width = 1, height = 2):
        object.__init__(self)
        self.setWidth(width)
        self.setHeight(height)

    #function to set width
    def setWidth(self, width):
        self.__width = width

    #function to get width
    def getWidth(self):
        return self.__width

    width = property(fget = getWidth, fset = setWidth)

    #function to set height
    def setHeight(self, height):
        self.__height = height

    #function to get height
    def getHeight(self):
        return self.__height

    height = property(fget = getHeight, fset = setHeight)

    #function to get area
    def getArea(self):
        return self.getWidth() * self.getHeight()

    area = property(fget = getArea)

    #function to get perimeter
    def getPerimeter(self):
        return 2*(self.getWidth() + self.getHeight())

    perimeter = property(fget = getPerimeter)

    #getStats function
    def getStats(self):
        print("width:     {}".format(self.width))
        print("height:    {}".format(self.height))
        print("area:      {}".format(self.area))
        print("perimeter: {}".format(self.perimeter))



def main():
    #prompt user for rectangle A dimensions
    w = input("Width of the first rectangle: ")
    h = input("Height of the first rectangle: ")
    
    #convert to floating point
    w1 = float(w)
    h1 = float(h)
    print ("")
    
    #initialize and print Rectangle A
    print ("Rectangle A:")
    a = Rectangle(w1, h1)
    print ("area:      {}".format(a.area))
    print ("perimeter: {}".format(a.perimeter))

    print ("")
    #prompt user for rectangle B dimensions
    w = input("Width of the second rectangle: ")
    h = input("Height of the second rectangle: ")
    
    #convert to floating point
    w2 = float(w)
    h2 = float(h)
    print ("")
    
    #initialize and print Rectangle B
    print ("Rectangle B:")
    b = Rectangle()
    b.width = w2
    b.height = h2
    print (b.getStats())

if __name__ == "__main__":
    main()