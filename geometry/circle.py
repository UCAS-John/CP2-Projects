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

    def display_info(self, nocalc=False):
        if nocalc:
            return f"Circle: Radius = {self.radius}"
        else:
            return f"Circle: Radius = {self.radius}, Area = {self.area()}, Perimeter = {self.perimeter()}"
    
    def draw_circle(self):
        fig, ax = plt.subplots()
        circle = patches.Circle((0, 0), self.radius, edgecolor='blue', facecolor='lightblue', linewidth=2)
        ax.add_patch(circle)
        ax.set_xlim(-self.radius * 1.5, self.radius * 1.5)
        ax.set_ylim(-self.radius * 1.5, self.radius * 1.5)
        ax.set_aspect('equal', adjustable='datalim')
        ax.annotate(f"Radius = {self.radius}", xy=(0, self.radius / 2), fontsize=10, ha='center')
        plt.title("Circle")
        plt.show()

    @staticmethod
    def explain_formulas():
        return "Area = π * radius^2, Perimeter = 2 * π * radius"
    
if __name__ == "__main__":
    circle = Circle(5)
    print(circle.display_info())
    circle.draw_circle()
    print(Circle.explain_formulas())