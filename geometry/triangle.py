import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Triangle:
    def __init__(self, side1, side2, side3):
        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            raise ValueError("All dimensions must be positive.")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    # Calculate area using Heron's formula
    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        area = (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5
        return area

    # Calculate perimeter
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    # Display information about the triangle if nocalc is False
    # Else display only the dimensions
    def display_info(self, nocalc=False):
        if nocalc:
            return f"Triangle: Side1 = {self.side1}, Side2 = {self.side2}, Side3 = {self.side3}"
        else:
            return f"Triangle: Side1 = {self.side1}, Side2 = {self.side2}, Side3 = {self.side3}, Area = {self.area()}, Perimeter = {self.perimeter()}"
    
    # Draw the triangle using matplotlib
    def draw_triangle(self):
        fig, ax = plt.subplots()

        # Define the three vertices of the triangle using side lengths
        
        # Vertex A is at (0, 0)
        A = (0, 0)

        # Vertex B is at (side1, 0) (horizontal distance)
        B = (self.side1, 0)

        # Vertex C is calculated using the law of cosines
        # cos C = (a^2 + b^2 - c^2) / (2ab)
        angle_C = math.acos((self.side1**2 + self.side2**2 - self.side3**2) / (2 * self.side1 * self.side2))
        
        # Polar Coordinates to Cartesian coordinates 
        # x = r * cos(theta)
        # y = r * sin(theta)
        # r is side 2 in this case and theta is angle C
        C = (self.side2 * math.cos(angle_C), self.side2 * math.sin(angle_C))

        # Create the triangle using the vertices
        vertices = [A, B, C]
        triangle = patches.Polygon(vertices, closed=True, edgecolor='red', facecolor='pink', linewidth=2)
        ax.add_patch(triangle)

        # Set plot limits to fit the triangle
        all_x = [A[0], B[0], C[0]]
        all_y = [A[1], B[1], C[1]]
        ax.set_xlim(min(all_x) - 1, max(all_x) + 1)
        ax.set_ylim(min(all_y) - 1, max(all_y) + 1)
        ax.set_aspect('equal', adjustable='datalim')

        # Add labels for the sides
        ax.annotate(f"Side1 = {self.side1}", xy=((A[0] + B[0]) / 2, (A[1] + B[1]) / 2 - 0.2), fontsize=10, ha='center')
        ax.annotate(f"Side2 = {self.side2}", xy=((A[0] + C[0]) / 2, (A[1] + C[1]) / 2), fontsize=10, ha='center')
        ax.annotate(f"Side3 = {self.side3}", xy=((B[0] + C[0]) / 2, (B[1] + C[1]) / 2), fontsize=10, ha='center')

        # Add title and show the plot
        plt.title("Triangle")
        plt.show()

    # Static method to explain the formulas for area and perimeter of Triangle
    @staticmethod
    def explain_formulas():
        return "Area = 0.5 * base * height, Perimeter = side1 + side2 + side3"
    
if __name__ == "__main__":
    triangle = Triangle(3, 9, 7)
    print(triangle.display_info())
    triangle.draw_triangle()
    print(Triangle.explain_formulas())