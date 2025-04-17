import math

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