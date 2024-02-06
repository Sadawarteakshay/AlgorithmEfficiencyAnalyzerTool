books = []
class Book:
    def __init__(self, title, author):  #This is the initializer method, __init__, for the Book class that takes title and author as parmeters.
        self.title = title
        self.author = author

    def __lt__(self, other):  #This method defines the less-than (<) operator for Book objects. 
        return self.author < other.author
    
def add_book(title, author):  # Define a function to add books.
    books.append(Book(title, author))

def unsorted_pile_of_books(): #show the list of books entered by the user
    for book in books:
        print(f"Title: {book.title}")
        print(f"Author: {book.author}")

def bubble_sort(books):  #sort the books based on author names using bubble sort
    n = len(books)
    for i in range(n):
        for j in range(0, n-i-1):
            if books[j] > books[j+1]:
                books[j], books[j+1] = books[j+1], books[j]
    return books

def sort_books(books): #show the list of sorted books
    books = bubble_sort(books)

    for book in books:
        print(f"Title: {book.title}")
        print(f"Author: {book.author}")

def main():
    while True:        # Start an infinite loop for the Command Line Interface (CLI).
        print("\nChoose action:")  # Prompt user to choose an action.
        print("1: Add Book")
        print("2: List Books")
        print("3: Sorted Books based on Author Names")
        print("4: Exit")

        choice = input()

        if(choice=="1"): # Check if the user wants to add a book.
            number_of_books = int(input("Enter the number of books: ")) 
            for k in range(number_of_books):
                title = input("Enter the title of the book: ")
                author = input("Enter the author of the book: ")
                add_book(title, author)

        elif(choice=="2"): #shows the list of books entered by the user
            print("\nUnsorted Books on the shelf:")
            unsorted_pile_of_books()

        elif(choice=="3"): #shows the list of books sorted bases on author names
            print("\nSorted Books based on author names:")
            sort_books(books)

        elif choice == "4": # Check if the user wants to exit.
            print("Bye!")
            break   # Exit the loop (and the program).

if __name__ == "__main__":
    main()        





