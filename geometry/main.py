from circle import Circle
from rectangle import Rectangle, Square
from triangle import Triangle
import sys

def main():
    shapes = []
    while True:
        print("\nGeometry Calculator")
        print("1. Create Circle")
        print("2. Create Rectangle")
        print("3. Create Square")
        print("4. Create Triangle")
        print("5. Display All Shapes")
        print("6. Visualize Shapes")
        print("7. Compare Shapes")
        print("8. Exit")
        choice = input("Enter your choice: ")

        try:
            match choice:
                # Create a Circle
                case '1':
                    radius = float(input("Enter radius: "))
                    shapes.append(Circle(radius))
                # Create a Rectangle
                case "2":
                    length = float(input("Enter length: "))
                    width = float(input("Enter width: "))
                    shapes.append(Rectangle(length, width))
                # Create a Square
                case "3":
                    side = float(input("Enter side length: "))
                    shapes.append(Square(side))
                # Create a Triangle
                case "4":
                    side1 = float(input("Enter side1: "))
                    side2 = float(input("Enter side2: "))
                    side3 = float(input("Enter side3: "))
                    shapes.append(Triangle(side1, side2, side3))
                # Display all shapes
                case "5":
                    print("\nShapes in the list:")
                    for shape in shapes:
                        print(shape.display_info())
                # Visualize shapes
                case "6":
                    print("\nShapes in the list:")
                    for i, shape in enumerate(shapes, start=1):
                        print(f"{i}. {shape.display_info(nocalc=True)}")

                    shape_choice = int(input("Select a shape to visualize: ")) - 1
                    if shape_choice < 0 or shape_choice >= len(shapes):
                        print("Invalid choice.")
                        continue
                    shape = shapes[shape_choice]
                    if isinstance(shape, Circle):
                        shape.draw_circle()
                    elif isinstance(shape, Rectangle):
                        shape.draw_rectangle()
                    elif isinstance(shape, Triangle):
                        shape.draw_triangle()
                    else:
                        print("Shape not supported for visualization.")

                # Compare shapes by selecting area or perimeter
                case "7":
                    if len(shapes) < 2:
                        print("At least two shapes are required for comparison.")
                        continue
                    print("1. Compare Areas")
                    print("2. Compare Perimeters")
                    compare_choice = input("Enter your choice: ")

                    if compare_choice not in ["1", "2"]:
                        print("Invalid choice.")
                        continue
                    
                    # Sort shapes based on the selected attribute
                    if compare_choice == "1":
                        shapes.sort(key=lambda s: s.area())
                        print("\nShapes sorted by area:")
                    elif compare_choice == "2":
                        shapes.sort(key=lambda s: s.perimeter())
                        print("\nShapes sorted by perimeter:")

                    for shape in shapes:
                        print(shape.display_info())

                case "8":
                    sys.exit(0)
                case _:
                    print("Invalid choice. Please try again.")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()