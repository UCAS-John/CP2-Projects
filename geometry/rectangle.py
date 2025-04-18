import matplotlib.pyplot as plt
import matplotlib.patches as patches

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
    def draw_rectangle(length, width):
        fig, ax = plt.subplots()
        rectangle = patches.Rectangle((-length / 2, -width / 2), length, width, edgecolor='green', facecolor='lightgreen', linewidth=2)
        ax.add_patch(rectangle)
        ax.set_xlim(-length, length)
        ax.set_ylim(-width, width)
        ax.set_aspect('equal', adjustable='datalim')
        ax.annotate(f"Length = {length}", xy=(0, width / 2 + 0.1), fontsize=10, ha='center')
        ax.annotate(f"Width = {width}", xy=(length / 2 + 0.1, 0), fontsize=10, rotation=90, va='center')
        plt.title("Rectangle")
        plt.show()

    @staticmethod
    def explain_formulas():
        return "Area = length * width, Perimeter = 2 * (length + width)"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def display_info(self):
        return f"Square: Side = {self.length}, Area = {self.area()}, Perimeter = {self.perimeter()}"

    def draw_square(side):
        Rectangle.draw_rectangle(side, side)  # A square is a special case of a rectangle

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