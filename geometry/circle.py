import math

class Circle:
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