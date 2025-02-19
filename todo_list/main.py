"""
OVERVIEW:
Create a program that allows the user to view, add, delete, and mark tasks on a to do list that is saved on a seperate text file. 

REQUIREMENTS:
Create a to do list (Kept on a txt file)
Add items to the to do list
Mark item as complete
Delete item from to do list
"""
def check_file():
    file_path = "todo_list/todo_list.txt"
    try:
        with open(file_path, "x"):
            return
    except FileExistsError:
        return 

def load(file_path: str):
    check_file()
    todo_list = {}
    with open(file_path, "r"):


def main():
    pass

if __name__ == "__main__":
    main()