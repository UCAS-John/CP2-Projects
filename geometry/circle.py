import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches

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
    
    def draw_circle(radius):
        fig, ax = plt.subplots()
        circle = patches.Circle((0, 0), radius, edgecolor='blue', facecolor='lightblue', linewidth=2)
        ax.add_patch(circle)
        ax.set_xlim(-radius * 1.5, radius * 1.5)
        ax.set_ylim(-radius * 1.5, radius * 1.5)
        ax.set_aspect('equal', adjustable='datalim')
        ax.annotate(f"Radius = {radius}", xy=(0, radius / 2), fontsize=10, ha='center')
        plt.title("Circle")
        plt.show()

    @staticmethod
    def explain_formulas():
        return "Area = π * radius^2, Perimeter = 2 * π * radius"