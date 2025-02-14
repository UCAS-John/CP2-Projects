import csv

# Load movies into dictionary
def load_movies(file_path):
    movies = []
    with open(file_path ,'r') as file:
        reader = csv.DictReader(file)

        # Add each movie dict to movies list
        for row in reader:
            row['Length (min)'] = int(row['Length (min)'])  # Convert length to integer
            movies.append(row)
    return movies

# Filtered Movies
def filter_movies(movies, genre=None, rating=None, director=None, length_range=None, actor=None):
    filtered_movies = movies
    
    if genre:
        filtered_movies = [movie for movie in filtered_movies if genre.lower() in movie['Genre'].lower()]
    if rating:
        filtered_movies = [movie for movie in filtered_movies if rating.lower() in movie['Rating'].lower()]
    if director:
        filtered_movies = [movie for movie in filtered_movies if director.lower() in movie['Director'].lower()]
    if length_range:
        min_length, max_length = length_range
        filtered_movies = [movie for movie in filtered_movies if min_length <= movie['Length (min)'] <= max_length]
    if actor:
        filtered_movies = [movie for movie in filtered_movies if actor.lower() in movie['Notable Actors'].lower()]
    
    return filtered_movies

# Print Table of Movies 
def print_movies(movies):
    # Check if there are no movies
    if not movies:
        print("Error: No movies")
        return
    
    # Check if all movies is in dictionary format
    if not all(isinstance(movie, dict) for movie in movies):
        print("Error: Invalid movie data format")
        return

    headers = ["Title", "Genre", "Rating", "Director", "Length (min)", "Notable Actors"]
    
    # Get max column width for each headers
    col_widths = {header: len(header) for header in headers} # Get length of each header to each header key
    for movie in movies:
        for header in headers:
            col_widths[header] = max(col_widths[header], len(str(movie.get(header, '')))) # Compare all string length in header and movies return the maximum

    # Print the header row 
    print(" | ".join(header.ljust(col_widths[header]) for header in headers))

    # Print seperate line below header
    print(" | ".join("-" * col_widths[header] for header in headers))

    # Print each movie row
    for movie in movies:
        print(" | ".join(str(movie.get(header, '')).ljust(col_widths[header]) for header in headers))


def main():
    file_path = "movies_list.csv"
    movies = load_movies(file_path) 
    
    while True:
        choice = input("1) Print all movies\n2) Recommend movies base on filter\n>>> ")
        match choice:
            # Print all movies
            case '1':
                print_movies(movies)

            # Print Filtered Movies
            case '2':                
                print("\nFilter options:")
                genre = input("Enter genre (press enter to skip) >>> ").strip() or None
                director = input("Enter director (press enter to skip) >>> ").strip() or None
                length_min = input("Enter minimum length in minutes (press enter to skip) >>> ")
                length_max = input("Enter maximum length in minutes (press enter to skip) >>> ")
                actor = input("Enter actor (press enter to skip) >>> ").strip() or None
                
                # Define length range as tuple of min and max length
                length_range = (int(length_min), int(length_max)) if length_min and length_max else None 
                
                results = filter_movies(movies, genre, director, length_range, actor) 
                
                # Check if filtered movie exits
                if results:
                    print("\nRecommended Movies:")
                    print_movies(results)
                else:
                    print("\nNo movies found with the given filtered\n")
            # Check for Invalid Choice
            case _:
                print("Error: Invalid choice")
                continue

if __name__ == "__main__":
    main()