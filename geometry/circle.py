import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Circle:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        self.radius = radius

    # Calculate area
    def area(self):
        return math.pi * self.radius ** 2

    # Calculate perimeter
    def perimeter(self):
        return 2 * math.pi * self.radius

    # Display information about the circle if nocalc is False
    # Else display only the dimensions
    def display_info(self, nocalc=False):
        if nocalc:
            return f"Circle: Radius = {self.radius}"
        else:
            return f"Circle: Radius = {self.radius}, Area = {self.area()}, Perimeter = {self.perimeter()}"
    
    # Draw the circle using matplotlib
    def draw_circle(self):
        fig, ax = plt.subplots()
        circle = patches.Circle((0, 0), self.radius, edgecolor='blue', facecolor='lightblue', linewidth=2) # Create a circle patch
        ax.add_patch(circle)

        # Set plot limits to fit the circle
        ax.set_xlim(-self.radius * 1.5, self.radius * 1.5)
        ax.set_ylim(-self.radius * 1.5, self.radius * 1.5)

        # Add labels for the radius
        ax.set_aspect('equal', adjustable='datalim')

        # Add radius text
        ax.annotate(f"Radius = {self.radius}", xy=(0, self.radius / 2), fontsize=10, ha='center')

        plt.title("Circle")
        plt.show()

    # Static method to explain the formulas for area and perimeter of Circle
    @staticmethod
    def explain_formulas():
        return "Area = π * radius^2, Perimeter = 2 * π * radius"
    
if __name__ == "__main__":
    circle = Circle(5)
    print(circle.display_info())
    circle.draw_circle()
    print(Circle.explain_formulas())