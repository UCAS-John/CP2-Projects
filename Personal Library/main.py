#John Wangwang Personal Libary

"""
Stores all items in a list
Function to add a new item
Function to search the items
Function to remove an item
Function that runs the code (displays the menu options inside and calls the functions inside of a while True loop)
Project must include
easy to understand variable and function names
Pseudocode comments explaining what the code is doing
Good use of white space to keep items separate and easy to read/find
Have at least 2 people test your code before submission!
"""

# Define the library as a list of tuples 
# Each tuple contains (title, author)

library = [
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "publication_date": "1960", "genre": "Fiction"},
    {"title": "1984", "author": "George Orwell", "publication_date": "1949", "genre": "Dystopian, Political Fiction"},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "publication_date": "1925", "genre": "Fiction, Tragedy"},
    {"title": "Moby-Dick", "author": "Herman Melville", "publication_date": "1851", "genre": "Adventure, Fiction"},
    {"title": "War and Peace", "author": "Leo Tolstoy", "publication_date": "1869", "genre": "Historical Fiction"},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "publication_date": "1813", "genre": "Romance, Fiction"},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "publication_date": "1951", "genre": "Fiction, Coming-of-Age"},
    {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "publication_date": "1954", "genre": "Fantasy"},
    {"title": "The Odyssey", "author": "Homer", "publication_date": "8th Century BC", "genre": "Epic Poetry"},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "publication_date": "1937", "genre": "Fantasy"},
    {"title": "Frankenstein", "author": "Mary Shelley", "publication_date": "1818", "genre": "Gothic Fiction, Horror"},
    {"title": "The Brothers Karamazov", "author": "Fyodor Dostoevsky", "publication_date": "1880", "genre": "Philosophical Fiction"},
    {"title": "Brave New World", "author": "Aldous Huxley", "publication_date": "1932", "genre": "Dystopian, Science Fiction"},
    {"title": "The Scarlet Letter", "author": "Nathaniel Hawthorne", "publication_date": "1850", "genre": "Historical Fiction"},
    {"title": "Crime and Punishment", "author": "Fyodor Dostoevsky", "publication_date": "1866", "genre": "Psychological Fiction"},
    {"title": "Anna Karenina", "author": "Leo Tolstoy", "publication_date": "1877", "genre": "Literary Fiction, Romance"},
    {"title": "Don Quixote", "author": "Miguel de Cervantes", "publication_date": "1605", "genre": "Literary Fiction, Satire"},
    {"title": "The Picture of Dorian Gray", "author": "Oscar Wilde", "publication_date": "1890", "genre": "Gothic Fiction"},
    {"title": "Jane Eyre", "author": "Charlotte Brontë", "publication_date": "1847", "genre": "Romance, Gothic Fiction"},
    {"title": "Wuthering Heights", "author": "Emily Brontë", "publication_date": "1847", "genre": "Gothic Fiction, Romance"},
    {"title": "Les Misérables", "author": "Victor Hugo", "publication_date": "1862", "genre": "Historical Fiction"},
    {"title": "The Divine Comedy", "author": "Dante Alighieri", "publication_date": "1320", "genre": "Epic Poetry"},
    {"title": "Dracula", "author": "Bram Stoker", "publication_date": "1897", "genre": "Gothic Horror"},
    {"title": "The Shining", "author": "Stephen King", "publication_date": "1977", "genre": "Horror"},
    {"title": "Fahrenheit 451", "author": "Ray Bradbury", "publication_date": "1953", "genre": "Dystopian, Science Fiction"},
    {"title": "Slaughterhouse-Five", "author": "Kurt Vonnegut", "publication_date": "1969", "genre": "Science Fiction, Satire"},
    {"title": "The Handmaid's Tale", "author": "Margaret Atwood", "publication_date": "1985", "genre": "Dystopian, Feminist Fiction"},
    {"title": "The Hunger Games", "author": "Suzanne Collins", "publication_date": "2008", "genre": "Dystopian, Science Fiction"},
    {"title": "The Fault in Our Stars", "author": "John Green", "publication_date": "2012", "genre": "Young Adult, Romance"},
    {"title": "The Maze Runner", "author": "James Dashner", "publication_date": "2009", "genre": "Dystopian, Science Fiction"},
    {"title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling", "publication_date": "1997", "genre": "Fantasy, Young Adult"},
    {"title": "The Girl on the Train", "author": "Paula Hawkins", "publication_date": "2015", "genre": "Thriller, Mystery"},
    {"title": "Gone Girl", "author": "Gillian Flynn", "publication_date": "2012", "genre": "Thriller, Mystery"},
    {"title": "The Da Vinci Code", "author": "Dan Brown", "publication_date": "2003", "genre": "Thriller, Mystery"},
    {"title": "The Alchemist", "author": "Paulo Coelho", "publication_date": "1988", "genre": "Fiction, Philosophical"},
    {"title": "Sapiens: A Brief History of Humankind", "author": "Yuval Noah Harari", "publication_date": "2011", "genre": "Non-fiction, History"},
    {"title": "The Power of Habit", "author": "Charles Duhigg", "publication_date": "2012", "genre": "Non-fiction, Self-help"},
    {"title": "Educated", "author": "Tara Westover", "publication_date": "2018", "genre": "Memoir"},
    {"title": "Becoming", "author": "Michelle Obama", "publication_date": "2018", "genre": "Memoir"},
    {"title": "The Art of War", "author": "Sun Tzu", "publication_date": "5th Century BC", "genre": "Philosophy, Military Strategy"},
    {"title": "Thinking, Fast and Slow", "author": "Daniel Kahneman", "publication_date": "2011", "genre": "Non-fiction, Psychology"},
    {"title": "Outliers", "author": "Malcolm Gladwell", "publication_date": "2008", "genre": "Non-fiction, Sociology"},
    {"title": "The Immortal Life of Henrietta Lacks", "author": "Rebecca Skloot", "publication_date": "2010", "genre": "Biography, Science"},
    {"title": "Quiet: The Power of Introverts in a World That Can't Stop Talking", "author": "Susan Cain", "publication_date": "2012", "genre": "Non-fiction, Psychology"},
    {"title": "The 7 Habits of Highly Effective People", "author": "Stephen R. Covey", "publication_date": "1989", "genre": "Self-help, Non-fiction"},
    {"title": "Atomic Habits", "author": "James Clear", "publication_date": "2018", "genre": "Self-help, Non-fiction"},
    {"title": "The Subtle Art of Not Giving a F*ck", "author": "Mark Manson", "publication_date": "2016", "genre": "Self-help, Non-fiction"},
    {"title": "Rich Dad Poor Dad", "author": "Robert T. Kiyosaki", "publication_date": "1997", "genre": "Personal Finance, Non-fiction"},
    {"title": "The Road", "author": "Cormac McCarthy", "publication_date": "2006", "genre": "Post-apocalyptic, Fiction"},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "publication_date": "1951", "genre": "Fiction, Coming-of-Age"},
    {"title": "The Chronicles of Narnia", "author": "C.S. Lewis", "publication_date": "1950", "genre": "Fantasy, Children's Literature"}
]

# Function to add a new item to the library catalog
def add_item():
    """
    Prompts the user for item details (title, author) and adds it to the catalog.
    Ensures no duplicate items are added.
    """
    print("\nAdd a New Item")
    title = input("Enter the title\n>>> ").strip()
    author = input("Enter the author\n>>> ").strip()
    date = input("Enter the first publication date\n>> ").strip()
    genre = input("Enter the genre\n>>> ")
    
    # Create a tuple for the new item
    item = {"title": title,
            "author": author,
            "publication_date": date,
            "genre": genre}
    
    # Add the new item to the catalog
    if item in library:
        print(f"\nItem '{title}' by '{author}' already exists in the catalog.\n")
    else:
        library.append(item)
        print(f"\nItem '{title}' by '{author}' added successfully!\n")

#Function to display all items in the library catalog
def display_items():

    print("\nLibrary Catalog Contents:")
    if not library:
        print("The library catalog is empty.\n")

    else:
        for index, book in enumerate(library):
            print(f"{index+1}. Title: {book["title"]}\n   Author: {book["author"]}\n   Publication date: {book["publication_date"]}\n   Genre: {book["genre"]}")
    print()

#Function to search for an item in the catalog by title or author
def search_item():

    print("\nSearch for an Item")
    query = input("Enter the title or author to search for: ").strip().lower()
    
    # store (title, author) in matches if it matches book in library
    matches = [(title, author) for title, author in library
               if query in title.lower() or query in author.lower()]

    if matches:
        print("\nSearch Results:")
        for index, (title, author) in enumerate(matches):
            print(f"{index+1}. Title: {title}, Author: {author}")
    else:
        print("\nNo matches found.\n")

def remove_item():
    """
    Function to remove an item from the catalog by title and author.
    Prompts the user for the title and author, and removes the matching item.
    """

    title_to_remove = input("Enter the title of the item to remove\n>>> ").strip()
    author_to_remove = input("Enter the author of the item to remove\n>>> ").strip()
    index = 0

    for i, book in enumerate(library):
        if book["title"] == title_to_remove and book["author"] == author_to_remove:
                index = i+1
    if not index:
        print(f"\nItem '{title_to_remove}' by '{author_to_remove}' not found in the library\n")
    else:
        library.remove(library[index-1])
        print(f"\nItem '{title_to_remove}' by '{author_to_remove}' removed successfully!\n")


def main():
    """
    Main function to display the menu and handle user input.
    Runs in a loop until the user chooses to exit.
    """
    while True:
        print("\nPersonal Library Catalog")
        print("1. Add a New Item")
        print("2. Display All Items")
        print("3. Search for an Item")
        print("4. Remove an Item")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5)\n>>> ")
        
        match choice:
            case '1':
                add_item()
            case '2':
                display_items()
            case '3':
                search_item()
            case '4':
                remove_item()
            case '5':
                print("\nExiting the program. Goodbye!\n")
                break
            case _:
                print("Please Enter number between 1-5")
                continue

if __name__ == "__main__":
    main()
