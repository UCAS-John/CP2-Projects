from circle import Circle
from rectangle import Rectangle, Square
from triangle import Triangle

def main():
    shapes = []
    while True:
        print("\nGeometry Calculator")
        print("1. Create Circle")
        print("2. Create Rectangle")
        print("3. Create Square")
        print("4. Create Triangle")
        print("5. Display All Shapes")
        print("6. Compare Shapes")
        print("7. Exit")
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                radius = float(input("Enter radius: "))
                shapes.append(Circle(radius))
            elif choice == "2":
                length = float(input("Enter length: "))
                width = float(input("Enter width: "))
                shapes.append(Rectangle(length, width))
            elif choice == "3":
                side = float(input("Enter side length: "))
                shapes.append(Square(side))
            elif choice == "4":
                base = float(input("Enter base: "))
                height = float(input("Enter height: "))
                side1 = float(input("Enter side1: "))
                side2 = float(input("Enter side2: "))
                side3 = float(input("Enter side3: "))
                shapes.append(Triangle(base, height, side1, side2, side3))
            elif choice == "5":
                for shape in shapes:
                    print(shape.display_info())
            elif choice == "6":
                if len(shapes) < 2:
                    print("At least two shapes are required for comparison.")
                    continue
                print("1. Compare Areas")
                print("2. Compare Perimeters")
                compare_choice = input("Enter your choice: ")
                if compare_choice == "1":
                    shapes.sort(key=lambda s: s.area())
                    print("Shapes sorted by area:")
                elif compare_choice == "2":
                    shapes.sort(key=lambda s: s.perimeter())
                    print("Shapes sorted by perimeter:")
                for shape in shapes:
                    print(shape.display_info())
            elif choice == "7":
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()