import math

class Point:
    'Repesents a point in 2D space'

    def __init__(self, x = 0, y = 0):
        """Initialize the point with x and y coordinates"""
        self.move(x, y)

    def move(self, x, y):
        """Move the point to a new location in 2D space"""
        self.x = x
        self.y = y
    
    def reset(self):
        """Reset the point to the origin (0, 0)"""
        self.move(0, 0)

    def calculate_distance(self, other_point):
        """Calculate the distance between this point and another point"""

        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) 

a = Point(3, 4)
b = Point(5, 6)
print(a.calculate_distance(b))    # Output: 5.0
print(a.calculate_distance(Point(0, 0)))  # Output: 5.0
print(a.move(11, 17))  # Output: None
print(a.calculate_distance(b))    # Output: 5.0

print(a)