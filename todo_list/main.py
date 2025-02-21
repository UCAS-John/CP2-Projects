"""
OVERVIEW:
Create a program that allows the user to view, add, delete, and mark tasks on a to do list that is saved on a seperate text file. 

REQUIREMENTS:
Create a to do list (Kept on a txt file)
Add items to the to do list
Mark item as complete
Delete item from to do list
"""
class TodoList:
    def __init__(self):
        self.file_path = "todo_list/todo_list.txt" # Todo list file path

    # Check if file exists
    def check_file(self):
        try:
            with open(self.file_path, "x"):
                return
        except FileExistsError:
            return 

    # Load file into dictionary
    def load(self):
        self.check_file()
        todo_list = {}
        try:
            with open(self.file_path, "r") as file:
                for line in file:
                    (todo, status) = line.split(", ")
                    todo_list[todo] = status
        except Exception as e:
            print(f"\nFile Read Error: {e}\n")
            return
        
        return todo_list

    # Write Todo list dictionary to file
    def write(self, todo_list: dict):
        try:
            with open(self.file_path, "w") as file:
                for todo, status in todo_list.items():
                    file.write(f"{todo}, {status}\n")
            return True
        except Exception as e:
            print(f"\nWrite Error : {e}\n")
            return False

    # Add Todo to file
    def add(self):
        self.check_file()
        while True:
            todo = input("\nDon't input comma\nEnter your todo to add >>> ")
            if "," in todo:
                continue
            else:
                break
        status = "Not-Complete"
        try:
            with open(self.file_path, "a") as file:
                file.write(f"{todo}, {status}\n")
            
            print(f"\nSuccesfully add {todo} to your todo list\n")
        except Exception as e:
            print(f"\nAdd Todo Error: {e}\n")

    # Remove Todo from file
    def remove(self):
        self.check_file()

        todo = input("\nEnter todo to remove >>> ")

        todo_list = {}
        todo_list = self.load()
        if todo not in todo_list:
            print("\nYou todo is not in todo list\n")
            return 
        todo_list.pop(todo)

        if self.write(todo_list):
            print(f"\nSuccesfully remove {todo} from your todo list\n")

    # Mark Todo if Compete or Not-Complete
    def mark(self):
        self.check_file()

        todo = input("\nEnter your todo to mark >>> ")
        status_input = input("1) Complete\n2) Not-Complete\nEnter status for your todo >>> ")

        match status_input:
            case '1':
                status = "Complete"
            case _:
                status = "Not-Complete"

        todo_list = {}
        todo_list = self.load()
        if todo not in todo_list:
            print("\nYou todo is not in todo list\n")
            return 
        else:
            todo_list[todo] = status

        if self.write(todo_list):
            print(f"\nSuccesfully mark {todo} as {status} from your todo list\n")

    # Clear all Todo in file
    def clear(self):
        self.check_file()
        try:
            with open(self.file_path, "w") as file:
                file.write("")
            print("\nSuccessfully clear todo list\n")
        except Exception as e:
            print(f"\nClear Todo List Error: {e}\n")

    # View all Todo in file
    def view(self):
        self.check_file()
        todo_list = {}
        todo_list = self.load()

        if not todo_list:
            print("\nYou don't have todo in your todo list yet\n")
            return
        
        headers = ["TO-DO", "STATUS"]

        # Get max column width for each headers
        col_widths = {header: len(header) for header in headers}

        # Get max column width for each todo and status
        for todo, status in todo_list.items():
            col_widths[headers[0]] = max(col_widths[headers[0]], len(str(todo)))
            col_widths[headers[1]] = max(col_widths[headers[0]], len(str(status))) 

        print("")
        # Print the header row 
        print(" | ".join(header.ljust(col_widths[header]) for header in headers))

        # Print seperate line below header
        print(" | ".join("-" * col_widths[header] for header in headers))

        # Print each Todo
        for (todo, status) in todo_list.items():
            task = str(todo).ljust(int(col_widths[headers[0]]))
            print(task, end="")
            print(f" | {status}")

        print("")

def main():

    todo_list = TodoList()

    instruction = "1) View Todo List\n2) Add Todo List\n3) Remove Todo List\n4) Clear all todo in todo list\n5) Exit"

    while True:
        print(instruction)
        choice = input("Enter action >>> ")

        match choice:
            # View all Todo
            case '1':
                todo_list.view()
            # Add Todo
            case '2':
                todo_list.add()
            # Remove Todo
            case '3':
                todo_list.remove()
            # Clear all Todo 
            case '4':
                todo_list.clear()
            # Exit
            case '5':
                print("Exit Todo List")
                break
            case _:
                print("Invalid Choice")

if __name__ == "__main__":
    main()