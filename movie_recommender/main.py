import csv

def load_movies(file_path):
    movies = []
    with open(file_path ,'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['Length (min)'] = int(row['Length (min)'])  # Convert length to integer
            movies.append(row)
    return movies

def filter_movies(movies, genre=None, director=None, length_range=None, actor=None):
    filtered_movies = movies
    
    if genre:
        filtered_movies = [movie for movie in filtered_movies if genre.lower() in movie['Genre'].lower()]
    if director:
        filtered_movies = [movie for movie in filtered_movies if director.lower() in movie['Director'].lower()]
    if length_range:
        min_length, max_length = length_range
        filtered_movies = [movie for movie in filtered_movies if min_length <= movie['Length'] <= max_length]
    if actor:
        filtered_movies = [movie for movie in filtered_movies if actor.lower() in movie['Actors'].lower()]
    
    return filtered_movies

def print_movies(movies):
    if not movies:
        print("Error: No movies")
        return
    
    if not all(isinstance(movie, dict) for movie in movies):
        print("Error: Invalid movie data format")
        return

    headers = ["Title", "Genre", "Director", "Length (min)", "Notable Actors"]
    
    # Determine column widths efficiently
    col_widths = {header: len(header) for header in headers}
    for movie in movies:
        for header in headers:
            col_widths[header] = max(col_widths[header], len(str(movie.get(header, ''))))

    # Print the header row
    print(" | ".join(header.ljust(col_widths[header]) for header in headers))

    # Print dynamic separator line
    print(" | ".join("-" * col_widths[header] for header in headers))

    # Print each movie row, handling multi-line values
    for movie in movies:
        print(" | ".join(str(movie.get(header, '')).replace("\n", ", ").ljust(col_widths[header]) for header in headers))


def main():
    file_path = "movies_list.csv"
    movies = load_movies(file_path)
    
    while True:
        choice = input("1) Print all movies\n2) Recommend movies base on filter\n>>> ")
        match choice:
            case '1':
                print_movies(movies)
            case '2':                
                print("\nFilter options:")
                genre = input("Enter genre (or press enter to skip) >>> ").strip() or None
                director = input("Enter director (or press enter to skip) >>> ").strip() or None
                length_min = input("Enter minimum length in minutes (or press enter to skip) >>> ")
                length_max = input("Enter maximum length in minutes (or press enter to skip) >>> ")
                actor = input("Enter actor (or press enter to skip) >>> ").strip() or None
                
                length_range = (int(length_min), int(length_max)) if length_min and length_max else None
                
                results = filter_movies(movies, genre, director, length_range, actor)
                
                if results:
                    print("\nRecommended Movies:")
                    print_movies(results)
                else:
                    print("\nNo movies found with the given criteria.")
            case _:
                print("Error: Invalid choice")
                return

if __name__ == "__main__":
    main()