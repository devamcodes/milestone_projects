"""
Project:database for milestone_2
Author:Devam A

"""
books = []
def add_book():
    user_input_add = input("enter the book name:")
    books.append(user_input_add)
    print("Book added to MY BOOKS")
    return books