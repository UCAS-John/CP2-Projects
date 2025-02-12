import csv

class File:
    def __init__(self, file_name):
        self.file_name = file_name
    
    def display(self, all=True, director=None, genre=None, Rating =None, length=None, actor=None):
        if all:
            with open(self.file_name, newline="") as file:
                movie_list = csv.reader(file)
                row_count = sum(1 for row in movie_list)
                for (index, movie) in enumerate(movie_list):
                    print(f"{index+1} | {'\t'.join(movie)}")
        else:
            with open(self.file_name, newline="") as file:
                movie_list = csv.reader(file)
                print(movie_list)

def search():
    question = "1) Director,\n2) Genre\n3) Rating\n4) Length\5n) Actor\n6) Go Back"

    while True:
        choice = input(question+"\n>>> ")

        match choice:
            case '1':
                pass
            case '2':
                pass
            case '3':
                pass
            case '4':
                pass
            case '5':
                pass
            case '6':
                return
            case _:
                print("Invalid Choice")
def main():

    file = File("movies_list.csv")

    while True:
        choice = input("1) Display all Movies\n2) Movie Recommendation\n>>> ")

        match choice:
            case '1':
                file.display()
            case '2':
                file.display(all=False)
            case _:
                print("Invalid Choice")
                continue

if __name__ == "__main__":
    main()