"""
Project:Book collection.
Author:Devam A

Description:book shop similar to apparel-shop
steps:
1. welcome message
2. main menu
    1.add book
    2.view list
    3.mark as read(make a new list)
    4.remove book
    5.exit program
3. def functions
4. database file import
5.
*Questions:
    1.how to creat a temporary database file
"""
MY_BOOKS = []


def add_book():
    user_input_add = input("enter the book name:")
    MY_BOOKS.append(user_input_add)
    print("Book added to MY BOOKS")
    return MY_BOOKS


def view_list():
    print(MY_BOOKS)


def mark_as_read():
    user_input_mark_read = input("enter the name of book to mark it as read:")
    #TODO:1. try-except loop is nit working properly
    try:
        mark_as_read_books = []
        if user_input_mark_read in MY_BOOKS:
            mark_as_read_books.append(user_input_mark_read)
            print(f"{user_input_mark_read} book is added to mark as read.")

    except:
        raise ValueError(f"{user_input_mark_read} book is not in your book list")
    else:
        print(mark_as_read_books)
def remove_book():
    #TODO:show the proper list of books with index
    print(MY_BOOKS)
    user_input_remove_book = int(input("enter the book index to remove the book:"))
    MY_BOOKS.pop(user_input_remove_book)
    print(f"{user_input_remove_book} is removed from the list.")



main_menu = """
1. Add book to MY BOOKS
2. View My BOOKS
3. Mark the book as read
4. Remove the book
5. Exit the program
enter the index number:"""
user_name = input("enter your name:")
print(f"Hello,{user_name}")
user_input_menu = int(input(main_menu))
while user_input_menu != 5:

    if user_input_menu == 1:
        add_book()
    elif user_input_menu == 2:
        view_list()
    elif user_input_menu == 3:
        mark_as_read()
    else:
        remove_book()
    user_input_menu = int(input(main_menu))
else:
    print("Exiting the program")