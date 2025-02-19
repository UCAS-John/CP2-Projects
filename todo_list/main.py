"""
OVERVIEW:
Create a program that allows the user to view, add, delete, and mark tasks on a to do list that is saved on a seperate text file. 

REQUIREMENTS:
Create a to do list (Kept on a txt file)
Add items to the to do list
Mark item as complete
Delete item from to do list
"""
def check_file(file_path: str):
    try:
        with open(file_path, "x") as file:
            return
    expect FileExistsError:
    

def main():
    pass

if __name__ == "__main__":
    main()