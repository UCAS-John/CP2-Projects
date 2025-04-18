import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Rectangle:
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive.")
        self.length = length
        self.width = width

    # Calculate area 
    def area(self):
        return self.length * self.width
    
    # Calculate perimeter
    def perimeter(self):
        return 2 * (self.length + self.width)

    # Display information about the rectangle if nocalc is False
    # Else display only the dimensions
    def display_info(self, nocalc=False):
        if nocalc:
            return f"Rectangle: Length = {self.length}, Width = {self.width}"
        else:
            return f"Rectangle: Length = {self.length}, Width = {self.width}, Area = {self.area()}, Perimeter = {self.perimeter()}"
    
    # Draw the rectangle using matplotlib
    def draw_rectangle(self):
        fig, ax = plt.subplots()
        rectangle = patches.Rectangle((-self.length / 2, -self.width / 2), self.length, self.width, edgecolor='green', facecolor='lightgreen', linewidth=2) # Create a rectangle patch
        ax.add_patch(rectangle)

        # Set plot limits to fit the rectangle
        ax.set_xlim(-self.length, self.length)
        ax.set_ylim(-self.width, self.width)

        # Add labels for the length and width
        ax.set_aspect('equal', adjustable='datalim')

        # Add length and width text
        ax.annotate(f"Length = {self.length}", xy=(0, self.width / 2 + 0.1), fontsize=10, ha='center')
        ax.annotate(f"Width = {self.width}", xy=(self.length / 2 + 0.1, 0), fontsize=10, rotation=90, va='center')
        
        plt.title("Rectangle")
        plt.show()

    # Static method to explain the formulas for area and perimeter of Rectangle
    @staticmethod
    def explain_formulas():
        return "Area = length * width, Perimeter = 2 * (length + width)"

# Create a subclass of Rectangle for Square
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    # Override the display_info method to show only the side length
    def display_info(self, nocalc=False):
        if nocalc:
            return f"Square: Side = {self.length}"
        else:
            return f"Square: Side = {self.length}, Area = {self.area()}, Perimeter = {self.perimeter()}"

    # Static method to explain the formulas for area and perimeter of Square
    @staticmethod
    def explain_formulas():
        return "Area = side^2, Perimeter = 4 * side"
    
if __name__ == "__main__":
    rectangle = Rectangle(4, 3)
    print(rectangle.display_info())
    rectangle.draw_rectangle()
    print(Rectangle.explain_formulas())

    square = Square(4)
    print(square.display_info())
    square.draw_rectangle()
    print(Square.explain_formulas())