import matplotlib.pyplot as plt
import matplotlib.patches as patches

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
    
    def draw_triangle(self):
        fig, ax = plt.subplots()
        # Define the three vertices of the triangle
        vertices = [(-self.base / 2, 0), (self.base / 2, 0), (0, self.height)]
        triangle = patches.Polygon(vertices, closed=True, edgecolor='red', facecolor='pink', linewidth=2) 
        ax.add_patch(triangle)
        ax.set_xlim(-self.base, self.base)
        ax.set_ylim(0, self.height * 1.5)
        ax.set_aspect('equal', adjustable='datalim')
        # Add labels for base and height
        ax.annotate(f"Base = {self.base}", xy=(0, -0.1), fontsize=10, ha='center')
        ax.annotate(f"Height = {self.height}", xy=(-self.base / 2 - 0.2, self.height / 2), fontsize=10, rotation=90, va='center')
        plt.title("Triangle")
        plt.show()

    @staticmethod
    def explain_formulas():
        return "Area = 0.5 * base * height, Perimeter = side1 + side2 + side3"
    
if __name__ == "__main__":
    triangle = Triangle(4, 3, 3, 4, 5)
    print(triangle.display_info())
    triangle.draw_triangle()
    print(Triangle.explain_formulas())