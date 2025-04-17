import math

class Triangle:
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