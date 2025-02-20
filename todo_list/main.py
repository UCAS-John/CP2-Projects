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
        self.file_path = "todo_list/todo_list.txt"

    def check_file(self):
        try:
            with open(self.file_path, "x"):
                return
        except FileExistsError:
            return 

    def load(self):
        self.check_file()
        todo_list = {}
        try:
            with open(self.file_path, "r") as file:
                for line in file:
                    (todo, status) = line.split()
                    todo_list[todo] = bool(status)
        except Exception as e:
            print(f"File Read Error: {e}")
            return
        
        return todo_list

    def write(self, todo_list: dict):
        try:
            with open(self.file_path, "w") as file:
                for todo, status in todo_list.items():
                    file.write(f"{todo} {status}\n")
            return True
        except Exception as e:
            print(f"Write Error : {e}")
            return False

    def add(self):
        self.check_file()
        todo = input("Enter your todo to add >>> ")
        status = False
        try:
            with open(self.file_path, "a") as file:
                file.write(f"{todo} {status}\n")
            
            print(f"Succesfully add {todo} to your todo list")
        except Exception as e:
            print(f"Add Todo Error: {e}")

    def remove(self):
        self.check_file()

        todo = input("Enter todo to remove >>> ")

        todo_list = {}
        todo_list = self.load()
        if todo not in todo_list:
            print("You todo is not in todo list")
            return 
        todo_list.pop(todo)

        if self.write(todo_list):
            print(f"Succesfully remove {todo} from your todo list")

    def mark(self):
        self.check_file()

        todo = input("Enter your todo to mark >>> ")
        while True:
            try:
                status = bool(input("Enter status for your todo (True/False) >>> "))
                break
            except ValueError:
                print("Please enter True or False")
                continue

        todo_list = {}
        todo_list = self.load()
        if todo not in todo_list:
            print("You todo is not in todo list")
            return 
        else:
            todo_list[todo] = status

        mark = "Not Complete"
        if status == True:
            mark = "Complete"

        if self.write(todo_list):
            print(f"Succesfully mark {todo} as {mark} from your todo list")

    def clear(self):
        self.check_file()
        try:
            with open(self.file_path, "w") as file:
                file.write("")
            print("Successfully clear todo list")
        except Exception as e:
            print(f"Clear Todo List Error: {e}")

    def view(self):
        self.check_file()
        todo_list = {}
        todo_list = self.load()

        if not todo_list:
            print("You don't have todo in your todo list yet")
            return
        for todo, status in todo_list.items():
            if status:
                mark = "Complete"
            else:
                mark = "Not Complete"

            print(f"Todo: {todo} Status: {mark}")

def main():

    todo_list = TodoList()

    instruction = "1) View Todo List\n2) Add Todo List\n3) Remove Todo List\n4) Clear all todo in todo list\n5) Exit"

    while True:
        print(instruction)
        choice = input("Enter action >>> ")

        match choice:
            case '1':
                todo_list.view()
            case '2':
                todo_list.add()
            case '3':
                todo_list.remove()
            case '4':
                todo_list.clear()
            case '5':
                print("Exit Todo List")
                break
            case _:
                print("Invalid Choice")

if __name__ == "__main__":
    main()