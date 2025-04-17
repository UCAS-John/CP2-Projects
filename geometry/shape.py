import math

class Shape:
    def display_info(self):
        raise NotImplementedError("This method should be implemented by subclasses.")

    @staticmethod
    def explain_formulas():
        raise NotImplementedError("This method should be implemented by subclasses.")


class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def display_info(self):
        return f"Circle: Radius = {self.radius}, Area = {self.area()}, Perimeter = {self.perimeter()}"

    @staticmethod
    def explain_formulas():
        return "Area = π * radius^2, Perimeter = 2 * π * radius"

class Ellipse(Shape):
    def __init__(self, semi_major_axis, semi_minor_axis):
        if semi_major_axis <= 0 or semi_minor_axis <= 0:
            raise ValueError("Semi-major and semi-minor axes must be positive.")
        self.semi_major_axis = semi_major_axis
        self.semi_minor_axis = semi_minor_axis

    def area(self):
        return math.pi * self.semi_major_axis * self.semi_minor_axis

    def perimeter(self):
        # Approximation using Ramanujan's formula
        h = ((self.semi_major_axis - self.semi_minor_axis) ** 2) / ((self.semi_major_axis + self.semi_minor_axis) ** 2)
        return math.pi * (self.semi_major_axis + self.semi_minor_axis) * (1 + (3 * h) / (10 + math.sqrt(4 - 3 * h)))

    def display_info(self):
        return f"Ellipse: Semi-major axis = {self.semi_major_axis}, Semi-minor axis = {self.semi_minor_axis}, Area = {self.area()}, Perimeter = {self.perimeter()}"

    @staticmethod
    def explain_formulas():
        return "Area = π * semi-major axis * semi-minor axis, Perimeter ≈ π * (semi-major axis + semi-minor axis) * (1 + (3h)/(10 + sqrt(4 - 3h)))"
    
class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3):
        if base <= 0 or height <= 0 or side1 <= 0 or side2 <= 0 or side3 <= 0:
            raise ValueError("All dimensions must be positive.")
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def display_info(self):
        return f"Triangle: Base = {self.base}, Height = {self.height}, Area = {self.area()}, Perimeter = {self.perimeter()}"

    @staticmethod
    def explain_formulas():
        return "Area = 0.5 * base * height, Perimeter = side1 + side2 + side3"
    
class EquilateralTriangle(Triangle):
    def __init__(self, side):
        if side <= 0:
            raise ValueError("Side must be positive.")
        super().__init__(side, (math.sqrt(3) / 2) * side, side, side, side)

    def display_info(self):
        return f"Equilateral Triangle: Side = {self.side1}, Area = {self.area()}, Perimeter = {self.perimeter()}"

    @staticmethod
    def explain_formulas():
        return "Area = (sqrt(3)/4) * side^2, Perimeter = 3 * side"

class IsoscelesTriangle(Triangle):
    def __init__(self, base, height, side):
        if base <= 0 or height <= 0 or side <= 0:
            raise ValueError("All dimensions must be positive.")
        super().__init__(base, height, side, side, base)

    def display_info(self):
        return f"Isosceles Triangle: Base = {self.base}, Height = {self.height}, Area = {self.area()}, Perimeter = {self.perimeter()}"

    @staticmethod
    def explain_formulas():
        return "Area = 0.5 * base * height, Perimeter = 2 * side + base"

class RightTriangle(Triangle):
    def __init__(self, base, height):
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive.")
        hypotenuse = math.sqrt(base ** 2 + height ** 2)
        super().__init__(base, height, base, height, hypotenuse)

    def display_info(self):
        return f"Right Triangle: Base = {self.base}, Height = {self.height}, Area = {self.area()}, Perimeter = {self.perimeter()}"

    @staticmethod
    def explain_formulas():
        return "Area = 0.5 * base * height, Perimeter = base + height + hypotenuse"
    
class Rectangle:
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive.")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def display_info(self):
        return f"Rectangle: Length = {self.length}, Width = {self.width}, Area = {self.area()}, Perimeter = {self.perimeter()}"

    @staticmethod
    def explain_formulas():
        return "Area = length * width, Perimeter = 2 * (length + width)"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def display_info(self):
        return f"Square: Side = {self.length}, Area = {self.area()}, Perimeter = {self.perimeter()}"

    @staticmethod
    def explain_formulas():
        return "Area = side^2, Perimeter = 4 * side"

class Rhombus(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def display_info(self):
        return f"Rhombus: Length = {self.length}, Width = {self.width}, Area = {self.area()}, Perimeter = {self.perimeter()}"

    @staticmethod
    def explain_formulas():
        return "Area = length * width, Perimeter = 2 * (length + width)"

class Parallelogram(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def display_info(self):
        return f"Parallelogram: Length = {self.length}, Width = {self.width}, Area = {self.area()}, Perimeter = {self.perimeter()}"

    @staticmethod
    def explain_formulas():
        return "Area = length * width, Perimeter = 2 * (length + width)"

class Trapezoid(Rectangle):
    def __init__(self, base1, base2, height):
        if base1 <= 0 or base2 <= 0 or height <= 0:
            raise ValueError("All dimensions must be positive.")
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def area(self):
        return 0.5 * (self.base1 + self.base2) * self.height

    def perimeter(self):
        return self.base1 + self.base2 + 2 * math.sqrt(self.height ** 2 + ((self.base2 - self.base1) / 2) ** 2)

    def display_info(self):
        return f"Trapezoid: Base1 = {self.base1}, Base2 = {self.base2}, Height = {self.height}, Area = {self.area()}, Perimeter = {self.perimeter()}"

    @staticmethod
    def explain_formulas():
        return "Area = 0.5 * (base1 + base2) * height, Perimeter = base1 + base2 + 2 * sqrt(height^2 + ((base2 - base1) / 2)^2)"
    
class Kite(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)

    def area(self):
        return 0.5 * self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def display_info(self):
        return f"Kite: Length = {self.length}, Width = {self.width}, Area = {self.area()}, Perimeter = {self.perimeter()}"

    @staticmethod
    def explain_formulas():
        return "Area = 0.5 * length * width, Perimeter = 2 * (length + width)"