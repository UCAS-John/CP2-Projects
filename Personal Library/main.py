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

# Personal Library Catalog Program

# Define the library as a set of tuples to store items
# Each tuple contains (title, creator)

library = {("Pride and Prejudice", "Jane Austen"),
    ("To Kill a Mockingbird", "Harper Lee"),
    ("The Great Gatsby", "F. Scott Fitzgerald"),
    ("One Hundred Years of Solitude", "Gabriel Garcia Marquez"),
    ("Moby Dick", "Herman Melville"),
    ("War and Peace", "Leo Tolstoy"),
    ("The Odyssey", "Homer"),
    ("Ulysses", "James Joyce"),
    ("Madame Bovary", "Gustave Flaubert"),
    ("The Divine Comedy", "Dante Alighieri"),
    ("Hamlet", "William Shakespeare"),
    ("The Catcher in the Rye", "J.D. Salinger"),
    ("The Brothers Karamazov", "Fyodor Dostoevsky"),
    ("Crime and Punishment", "Fyodor Dostoevsky"),
    ("Wuthering Heights", "Emily Brontë"),
    ("Jane Eyre", "Charlotte Brontë"),
    ("The Iliad", "Homer"),
    ("1984", "George Orwell"),
    ("The Adventures of Huckleberry Finn", "Mark Twain"),
    ("Anna Karenina", "Leo Tolstoy"),
    ("Alice's Adventures in Wonderland", "Lewis Carroll"),
    ("The Sound and the Fury", "William Faulkner"),
    ("Great Expectations", "Charles Dickens"),
    ("Catch-22", "Joseph Heller"),
    ("The Grapes of Wrath", "John Steinbeck"),
    ("Invisible Man", "Ralph Ellison"),
    ("Don Quixote", "Miguel de Cervantes"),
    ("Beloved", "Toni Morrison"),
    ("Mrs. Dalloway", "Virginia Woolf"),
    ("The Scarlet Letter", "Nathaniel Hawthorne"),
    ("Brave New World", "Aldous Huxley"),
    ("The Sun Also Rises", "Ernest Hemingway"),
    ("Slaughterhouse-Five", "Kurt Vonnegut"),
    ("Lolita", "Vladimir Nabokov"),
    ("Middlemarch", "George Eliot"),
    ("The Picture of Dorian Gray", "Oscar Wilde"),
    ("Frankenstein", "Mary Shelley"),
    ("The Count of Monte Cristo", "Alexandre Dumas"),
    ("Les Misérables", "Victor Hugo"),
    ("The Hobbit", "J.R.R. Tolkien"),
    ("Fahrenheit 451", "Ray Bradbury"),
    ("The Stranger", "Albert Camus"),
    ("Heart of Darkness", "Joseph Conrad"),
    ("The Old Man and the Sea", "Ernest Hemingway"),
    ("A Tale of Two Cities", "Charles Dickens"),
    ("Gulliver's Travels", "Jonathan Swift"),
    ("The Trial", "Franz Kafka"),
    ("The Red Badge of Courage", "Stephen Crane"),
    ("The Secret Garden", "Frances Hodgson Burnett"),
    ("The Jungle", "Upton Sinclair"),
    ("The Call of the Wild", "Jack London"),
    ("The Metamorphosis", "Franz Kafka"),
    ("The Idiot", "Fyodor Dostoevsky"),
    ("The Master and Margarita", "Mikhail Bulgakov"),
    ("The Three Musketeers", "Alexandre Dumas"),
    ("Dracula", "Bram Stoker"),
    ("The Lord of the Rings", "J.R.R. Tolkien"),
    ("Rebecca", "Daphne du Maurier"),
    ("Gone with the Wind", "Margaret Mitchell"),
    ("The Little Prince", "Antoine de Saint-Exupéry"),
    ("The Bell Jar", "Sylvia Plath"),
    ("The Catcher in the Rye", "J.D. Salinger"),
    ("The Grapes of Wrath", "John Steinbeck"),
    ("The Picture of Dorian Gray", "Oscar Wilde"),
    ("The Kite Runner", "Khaled Hosseini"),
    ("Life of Pi", "Yann Martel"),
    ("The Book Thief", "Markus Zusak"),
    ("The Road", "Cormac McCarthy"),
    ("The Alchemist", "Paulo Coelho"),
    ("The Handmaid's Tale", "Margaret Atwood"),
    ("The Hitchhiker's Guide to the Galaxy", "Douglas Adams"),
    ("The Shining", "Stephen King"),
    ("The Da Vinci Code", "Dan Brown"),
    ("The Girl with the Dragon Tattoo", "Stieg Larsson"),
    ("The Hunger Games", "Suzanne Collins"),
    ("Harry Potter and the Sorcerer's Stone", "J.K. Rowling"),
    ("The Fault in Our Stars", "John Green"),
    ("The Help", "Kathryn Stockett"),
    ("The Lovely Bones", "Alice Sebold"),
    ("The Time Traveler's Wife", "Audrey Niffenegger"),
    ("The Secret Life of Bees", "Sue Monk Kidd"),
    ("The Curious Incident of the Dog in the Night-Time", "Mark Haddon"),
    ("The Perks of Being a Wallflower", "Stephen Chbosky"),
    ("The Giver", "Lois Lowry"),
    ("The Outsiders", "S.E. Hinton"),
    ("The Maze Runner", "James Dashner"),
    ("Divergent", "Veronica Roth"),
    ("Twilight", "Stephenie Meyer"),
    ("The Chronicles of Narnia", "C.S. Lewis"),
    ("The Great Gatsby", "F. Scott Fitzgerald"),
    ("To Kill a Mockingbird", "Harper Lee"),
    ("Pride and Prejudice", "Jane Austen"),
    ("1984", "George Orwell"),
    ("The Catcher in the Rye", "J.D. Salinger"),
    ("The Lord of the Rings", "J.R.R. Tolkien"),
    ("The Hobbit", "J.R.R. Tolkien"),
    ("Fahrenheit 451", "Ray Bradbury"),
    ("Jane Eyre", "Charlotte Brontë"),
    ("Wuthering Heights", "Emily Brontë"),
    ("The Odyssey", "Homer"),
    ("Moby Dick", "Herman Melville"),
    ("War and Peace", "Leo Tolstoy"),
    ("Crime and Punishment", "Fyodor Dostoevsky"),
    ("The Divine Comedy", "Dante Alighieri"),
    ("Hamlet", "William Shakespeare"),
    ("The Iliad", "Homer"),
    ("One Hundred Years of Solitude", "Gabriel Garcia Marquez"),
    ("The Brothers Karamazov", "Fyodor Dostoevsky"),
    ("Brave New World", "Aldous Huxley"),
    ("The Sun Also Rises", "Ernest Hemingway"),
    ("Slaughterhouse-Five", "Kurt Vonnegut"),
    ("Lolita", "Vladimir Nabokov"),
    ("Middlemarch", "George Eliot"),
    ("Frankenstein", "Mary Shelley"),
    ("The Count of Monte Cristo", "Alexandre Dumas"),
    ("Les Misérables", "Victor Hugo"),
    ("The Old Man and the Sea", "Ernest Hemingway"),
    ("A Tale of Two Cities", "Charles Dickens"),
    ("Gulliver's Travels", "Jonathan Swift")}

#Function to add a new item to the library catalog
def add_item():
    """
    Prompts the user for item details (title, creator) and adds it to the catalog.
    Ensures no duplicate items are added.
    """
    print("\nAdd a New Item")
    title = input("Enter the title: ").strip()
    creator = input("Enter the author/artist/director: ").strip()
    
    # Create a tuple for the new item
    item = (title, creator)
    
    # Attempt to add the new item to the catalog
    if item in library:
        print(f"\nItem '{title}' by '{creator}' already exists in the catalog.\n")
    else:
        library.add(item)
        print(f"\nItem '{title}' by '{creator}' added successfully!\n")

#Function to display all items in the library catalog
def display_items():

    print("\nLibrary Catalog Contents:")
    if not library:
        print("The library catalog is empty.\n")
    else:
        for index, (title, creator) in enumerate(library, start=1):
            print(f"{index}. Title: {title}, Author/Artist/Director: {creator}")
    print()

#Function to search for an item in the catalog by title or creator
def search_item():

    print("\nSearch for an Item")
    query = input("Enter the title or author/artist/director to search for: ").strip().lower()
    matches = [(title, creator) for title, creator in library
               if query in title.lower() or query in creator.lower()]

    if matches:
        print("\nSearch Results:")
        for index, (title, creator) in enumerate(matches, start=1):
            print(f"{index}. Title: {title}, Author/Artist/Director: {creator}")
    else:
        print("\nNo matches found.\n")

def remove_item():
    """
    Function to remove an item from the catalog by title and creator.
    Prompts the user for the title and creator, and removes the matching item.
    """
    
    print("\nRemove an Item")
    title_to_remove = input("Enter the title of the item to remove: ").strip()
    creator_to_remove = input("Enter the author/artist/director of the item to remove: ").strip()
    
    item_to_remove = (title_to_remove, creator_to_remove)
    
    if item_to_remove in library:
        library.remove(item_to_remove)
        print(f"\nItem '{title_to_remove}' by '{creator_to_remove}' removed successfully!\n")
    else:
        print(f"\nItem '{title_to_remove}' by '{creator_to_remove}' not found in the catalog.\n")

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
        
        while True:
            try:
                choice = int(input("\nEnter your choice (1-5): ")).strip()
            except ValueError:
                print("Enter a number between 1-5")
                continue

            if choice not in range(1,6):
                print("Enter number between 1-5")
                continue
            else:
                break
        
        match choice:
            case 1:
                add_item()
            case 2:
                display_items()
            case 3:
                search_item()
            case 4:
                remove_item()
            case 5:
                print("\nExiting the program. Goodbye!\n")
                break

if __name__ == "__main__":
    main()
