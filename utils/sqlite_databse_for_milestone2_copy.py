from .database_connection import DatabaseConnection


def create_books_tables():
    with DatabaseConnection('database_for_milestone2.db') as connection:
        cursor = connection.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')


def add_book(name, author):
    with DatabaseConnection('database_for_milestone2.db') as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (name, author))
        #could have used fstring in the above execute but it makes program very vulnerable .

def view_books():
    with DatabaseConnection('database_for_milestone2.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM books ')


        books = [{"name":row[0], "author":row[1], "read": row[2]} for row in cursor.fetchall()]
        return  books

def mark_as_read(name):
    with DatabaseConnection('database_for_milestone2.db') as connection:
        cursor = connection.cursor()

        cursor.execute('UPDATE books SET read = 1 WHERE name = ?', (name,))


def mark_as_unread(name):
    with DatabaseConnection('database_for_milestone2.db') as connection:
        cursor = connection.cursor()

        cursor.execute('UPDATE books SET read = 0 WHERE name = ?', (name,))


def remove_book(name):
    with DatabaseConnection('database_for_milestone2.db') as connection:
        cursor = connection.cursor()

        cursor.execute('DELETE FROM books WHERE name = ?',(name,))

