books = ["Python", "Java", "C++"]

while True:
    print("1. Add book")
    print("2. Search book")
    print("3. Remove book")
    print("4. Display books")
    print("5. Count books")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        book = input("Enter book name: ")
        books.append(book)

    elif choice == 2:
        book = input("Search book: ")
        if book.lower() in [b.lower() for b in books]:
            print("Book found")
        else:
            print("Book not found")

    elif choice == 3:
        book = input("Enter book to remove: ")
        for b in books:
            if b.lower() == book.lower():
                books.remove(b)
                break
        else:
            print("Book not found")

    elif choice == 4:
        print("Books:", books)

    elif choice == 5:
        print("Total books:", len(books))

    elif choice == 6:
        break

    else:
        print("Invalid choice")