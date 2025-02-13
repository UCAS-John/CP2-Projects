import csv 
import pandas as pd
class FileCSV:
    def __init__(self, file_name):
        self.file_name = file_name
    
    def display(self, all=True, director=None, genre=None, rating =None, length=None, actor=None):
        with open(self.file_name, newline="") as file:
            movie_list = csv.reader(file, delimiter = ',')
            if all:
                    for (index, movie) in enumerate(movie_list):
                        print(f"{index+1} | {movie}")
            else:
                if director != None:
                    for (index, movie) in enumerate(movie_list):
                        print(f"{movie}")
                        break
                    for (index, movie) in enumerate(movie_list):
                        if director in movie[1]:
                            print(f"{index+1} | {movie}")
                elif genre != None:
                    for (index, movie) in enumerate(movie_list):
                        print(f"{movie}")
                        break
                    for (index, movie) in enumerate(movie_list):
                        if genre in movie[2]:
                            print(f"{index+1} | {movie}")   
                elif rating != None:
                    for (index, movie) in enumerate(movie_list):
                        print(f"{movie}")
                        break
                    for (index, movie) in enumerate(movie_list):
                        if rating in movie[3]:
                            print(f"{index+1} | {movie}")   
                elif length != None:
                    for (index, movie) in enumerate(movie_list):
                        print(f"{movie}")
                        break
                    for (index, movie) in enumerate(movie_list):
                        if length in movie[4]:
                            print(f"{index+1} | {movie}")   
                elif actor != None:
                    for (index, movie) in enumerate(movie_list):
                        print(f"{movie}")
                        break
                    for (index, movie) in enumerate(movie_list):
                        if actor in movie[5]:
                            print(f"{index+1} | {movie}")   
                else:
                    print("Error: display() expected argument")
                    return            

    def recommendation(self):
        question = "1) Director,\n2) Genre\n3) Rating\n4) Length\n5) Actor\n6) Go Back"

        while True:
            choice = input(question+"\n>>> ")
            sec_choice = input("Enter second filter\n>>> ")

            if not sec_choice in range(1,6):
                sec_choice = None
            else:
                match choice, sec_choice:
                    case '1':
                        director_name = input("Enter Director name\n>>> ")
                        self.display(all=False, director=director_name)
                    case '2':
                        genre = input("Enter Genre\n>>> ")
                        self.display(all=False, genre=genre)
                    case '3':
                        rating = input("Enter Rating\n>>> ")
                        self.display(all=False, rating=rating)
                    case '4':
                        length = input("Enter length of the movie\n>>> ")
                        self.display(all=False, length=length)
                    case '5':
                        actor_name = input("Enter Actor name\n>>> ")
                        self.display(all=False, actor=actor_name)
                    case '6':
                        return
                    case _:
                        print("Invalid Choice")
def main():

    file = FileCSV("movies_list.csv")

    while True:
        choice = input("1) Display all Movies\n2) Movie Recommendation\n>>> ")

        match choice:
            case '1':
                file.display()
            case '2':
                file.recommendation()
            case _:
                print("Invalid Choice")
                continue

if __name__ == "__main__":
    main()