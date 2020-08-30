My_Books = []


def add_book(name, author):
    My_Books.append({'name': name, 'author': author, 'read': False})


def view_books():
    return My_Books


def mark_as_read(name):
    for books in My_Books:
        if books['name'] == name:
            books['read'] = True


def remove_book(name):
    """for books in My_Books:
      if books['name'] == name:
            My_Books.remove(name)
       """
    global My_Books
    My_Books = [books for books in My_Books if books['name'] != name ]