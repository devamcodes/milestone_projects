"""
Project:Movie collection app.
Author:Devam A

Description:
**This program needs database.


Status:(THIS PROJECT IS MADE TO SUCCESS)SUCCESSFUL

changes to be made:
*DONE 1. if movie is not found then error message should be shown
*DONE 2. after te termination of the program it should show the ending message and close it
*DONE 3. error handling should be added to enter the name
*DONE 4. pressing 2 for termination of the program it should close the program
"""
def enter_user_name():
    user_name = input("PLEASE ENTER YOUR NAME:")
    user_name_booleane = bool(user_name)
    if user_name_booleane == True:
        print(f"Hello, {user_name.title()}")
    else:
        input("program terminated!!")
        raise ValueError("Invalid input please enter a valid name:")



movies = []
find_movie_name = []


def find_movie_option():
    #To Do:1
    find_movie = input("ENTER MOVIE NAME:")
    if find_movie in movies:
        print(f"We have found the movie in your movie collection:-> {find_movie.title()}")
    else:
        raise ValueError("THIS MOVIE IS NOT IN YOUR COLLECTION,TRY AGAIN!")




menu_option = """
Please enter the option number:
  0. Add Movie
  1. View MovieList
  2. Find Movie
-->"""

def add_movie():
    
    user_input_movies = input("PLEASE ENTER A MOVIE NAME:")
    movies.append(user_input_movies)
    output = print("THE MOVIE IS ADDED TO THE COLLECTION.")
    return output


enter_user_name()
user_conformation = int(input("TO CONTINUE TYPE 0 OR ENTER 1 TO TERMINATE THE ROGRAM:"))
if user_conformation == 0:
    while user_conformation == 0:
        #TODO:if enter is pressed instead of any number then raise an error.
        user_input = int(input(menu_option))
        if user_input == 0:
            add_movie()

        elif user_input == 1:
            print(movies)
        elif user_input == 2:
            find_movie_option()
        else:
            print("INVALID INPUT PLEASE TRY AGAIN:")

        user_conformation = int(input("TO CONTINUE TYPE 0 OR ENTER 1 TO TERMINATE THE PROGRAM:"))
    else:
        input("Thank You!! come again and have a nice day!! PRESS ENTER.")
        print("PROGRAM COMPLETED.")
elif user_conformation == 1:
    print("program terminated by the user")
else:
    raise ValueError("Invalid input. please try again..")
