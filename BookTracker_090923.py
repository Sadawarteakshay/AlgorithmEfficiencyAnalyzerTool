books = []          # Create an empty list to store book details.

genres = {          # Dictionary mapping genre numbers to genre names.
    1: "Fiction",
    2: "Non-Fiction",
    3: "Biography",
    4: "Mystery",
    5: "Fantasy"
}

def add_book(title, author, genre_num, rating):  # Define a function to add books.
    genre = genres.get(genre_num, "Unknown")     # Get the genre name using its number.
    books.append({                               # Append the book details to the 'books' list.
        'title': title,
        'author': author,
        'genre': genre,
        'rating': rating
    })

def list_books():               # Define a function to list all books.
    for book in books:          # Loop through each book in the list.
        print("\n---------")
        print(f"Title: {book['title']}")    # Print the title of the book.
        print(f"Author: {book['author']}")  # Print the author of the book.
        print(f"Genre: {book['genre']}")    # Print the genre of the book.
        print(f"Rating: {book['rating']}")  # Print the rating of the book.
        print("---------\n")

def find_book(title):              # Define a function to find a book by title.
    for book in books:             # Loop through each book in the list.
        if book['title'].lower() == title.lower():  # Compare the book title in a case-insensitive manner.
            return book             # Return the book details if found.
    return None                   # Return None if no match is found.

def delete_book(title):                       # Define a function to delete a book by title.
    global books                              # Declare 'books' as a global variable.
    books = [book for book in books if book['title'].lower() != title.lower()]  # Filter out the book to be deleted.

while True:        # Start an infinite loop for the Command Line Interface (CLI).
    print("\nChoose action:")  # Prompt user to choose an action.
    print("1: Add Book")
    print("2: List Books")
    print("3: Find Book")
    print("4: Delete Book")
    print("5: Exit")
    
    choice = input()   # Take user input to decide the action.

    if choice == "1":  # Check if the user wants to add a book.
        title = input("\nEnter book title: ")
        author = input("Enter author: ")
        print("Select genre:")
        for num, genre in genres.items():    # Display available genres.
            print(f"{num}: {genre}")
        genre_num = int(input())             # Take genre number as input.
        rating = input("Enter rating (1 to 5): ")
        add_book(title, author, genre_num, rating)  # Add the book using the details.

    elif choice == "2":  # Check if the user wants to list all books.
        list_books()

    elif choice == "3":  # Check if the user wants to find a book.
        title = input("\nEnter book title to find: ")
        book = find_book(title)
        if book:
            print("\n---------")
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Genre: {book['genre']}")
            print(f"Rating: {book['rating']}")
            print("---------\n")
        else:
            print("\nBook not found.\n")

    elif choice == "4":  # Check if the user wants to delete a book.
        title = input("\nEnter book title to delete: ")
        delete_book(title)

    elif choice == "5":  # Check if the user wants to exit.
        break            # Exit the loop (and the program).
