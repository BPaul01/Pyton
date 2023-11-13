import math
#ex1
class Shape:
    #those functions will be overwritten
    def print_class_name():
        print("Shape")
    def calculate_area(self):
        pass
    def calculate_perimeter(self):
        pass

class Circle(Shape):
    pi = 3.14159

    def __init__(self, radius):
        if radius < 0:
            return "Error: Radius can't be < 0"

        super().__init__()
        self.radius = radius
        self.diameter = 2 * radius

    def print_class_name():
        print("Circle")

    #the circle doesn't have area
    def calculate_disk_area(self):
        return self.radius * Circle.pi

    def calculate_perimeter(self):
        return 2 * Circle.pi * self.radius

class Rectangle(Shape):
    def __init__(self, height, lenght):
        if height < 0:
            return "Error: Height can't be < 0"
        if lenght < 0:
            return "Error: Length can't be < 0"

        super().__init__()
        self.height = height
        self.length = lenght

    def print_class_name():
        print("Rectangle")

    def calculate_area(self):
        return self.length * self.height

    def calculate_perimeter(self):
        return 2 * self.length + 2 * self.height

class Triangle(Shape):
    def __init__(self, a, b, c):
        if not (a + b > c and b + c > a and c + a > b):
            return "Error: The given edges can't make a triangle"

        super().__init__()
        self.a = a
        self.b = b
        self.c = c

    def print_class_name():
        print("Triangle")

    def calculate_area(self):
        semi_parameter = self.calculate_perimeter() / 2
        return math.sqrt(semi_parameter * (semi_parameter - self.a) * (semi_parameter - self.b) * (semi_parameter - self.c))

    def calculate_perimeter(self):
        return self.a + self.b + self.c

def main():
    #ex1
    c = Circle(2)
    Circle.print_class_name()
    print("Disk area:", c.calculate_disk_area())
    print("Circle perimeter:", c.calculate_perimeter())
    print()

    r = Rectangle(2, 3)
    Rectangle.print_class_name()
    print("Rectangle area:", r.calculate_area())
    print("Rectangle perimeter:", r.calculate_perimeter())
    print()

    t = Triangle(4, 5, 6)
    Triangle.print_class_name()
    print("Triangle area:", t.calculate_area())
    print("Triangle perimeter:", t.calculate_perimeter())

if __name__ == "__main__":
    main()