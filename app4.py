from copy import copy

class Point:
    """Represents a point in 2D space."""

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'Point({self.x}, {self.y})'
    
    def __eq__(self, value):
        return isinstance(value, Point) and self.x == value.x and self.y == value.y

    def translate(self, dx=0, dy=0):
        """Translates the point by dx and dy."""
        point = copy(self)
        point.x += dx
        point.y += dy
        return point


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        
    def __str__(self):
        return f'Line({self.p1}, {self.p2})'
    

if __name__ == "__main__":
    start = Point(0, 0)
    print(start)  # Output: Point(0, 0)

    end2 = start.translate(0, 150)
    print(end2)  # Output: Point(0, 150)

    print(start)  # Output: Point(0, 0) - original point remains unchanged

    p1 = Point(200, 100)
    p2 = Point(200, 100)
    print(p1 == p2)  # Output: True 
    print(p1 is p2)  # Output: False - different instances

    line = Line(Point(0, 0), Point(100, 100))
    print(line)  # Output: Line(Point(0, 0), Point(100, 100))