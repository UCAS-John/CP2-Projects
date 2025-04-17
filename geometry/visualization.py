import matplotlib.pyplot as plt
import matplotlib.patches as patches

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

def draw_square(side):
    draw_rectangle(side, side)  # A square is a special case of a rectangle

if __name__ == "__main__":
    print("Shape Visualization")
    print("1. Draw Circle")
    print("2. Draw Rectangle")
    print("3. Draw Square")
    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            radius = float(input("Enter radius: "))
            draw_circle(radius)
        elif choice == "2":
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))
            draw_rectangle(length, width)
        elif choice == "3":
            side = float(input("Enter side length: "))
            draw_square(side)
        else:
            print("Invalid choice.")
    except ValueError as e:
        print(f"Error: {e}")