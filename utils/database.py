My_Books = "books.txt"


def add_book(name, author):
    with open(My_Books, 'a') as file:
        file.write(f"{name},{author},0\n")


def view_books():
    with open(My_Books, 'r') as file:
        lines = [line.strip().split(",") for line in file.readlines()]

    return [
        {'name':line[0], 'author':line[1], 'read':line[2]}
        for line in lines
        ]

def mark_as_read(name):
    books = view_books()
    for book in books:
        if book['name'] == name:
            book['read'] = 1
        else:
            raise ValueError("Book not found!!!")
    _save_the_books(books)


def _save_the_books(books):
    with open(My_Books, 'w') as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}\n")


def mark_as_unread(name):
    books = view_books()
    for book in books:
        if book['name'] == name:
            if book['name'] == name:
                book['read'] = 0
        else:
            raise ValueError("Book not found!!!")
    _save_the_books(books)


def remove_book(name):
    books = view_books()
    books = [book for book in books if book['name'] != name]
    _save_the_books(books)
"""
    global My_Books
    My_Books = [books for books in My_Books if books['name'] == name]
 """