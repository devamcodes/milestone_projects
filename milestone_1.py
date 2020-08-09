"""
Project:Make a movie collection app.
Author:Devam A
Description:
this program take input for movies and makes the list of them and then prints out the list if invalid input is given then it shows error.
this program lacks in saving the data when its finished due to use of list instead of database.
Status:Failed
changes to be made:
1. if movie is not found then error message should be shown
*DONE 2. after te termination of the program it should show the ending message and close it
3. error handling should be added to enter the name
*DONE 4. pressing 2 for termination of the program it should close the program
"""
def enter_user_name():
    user_name = input("PLEASE ENTER YOUR NAME:")
    user_name_booleane = bool(user_name)
    if user_name_booleane == True:
        print(f"Hello, {user_name.title()}")
    else:
        raise ValueError("Invalid input please enter a name:")


movies = []


def find_movie():
    #To Do:1
    find_movie = input("ENTER MOVIE NAME:")
    for movie in movies:
        if find_movie.title() == movie.title():
            print(movie)
        else:
            raise ValueError("THIS MOVIE IS NOT IN YOUR COLLECTION,TRY AGAIN!")

menu_option = """
Please enter the option number:
  0. Add Movie
  1. View MovieList
  2. Find Movie
  3. Quit Program
-->"""

def add_movie():
    
    user_input_movies = input("PLEASE ENTER A MOVIE NAME:")
    movies.append(user_input_movies)
    output = print("THE MOVIE IS ADDED TO THE COLLECTION.")
    return output


enter_user_name()
user_conformation = int(input("TO CONTINUE TYPE 1 OR ENTER 2 TO TERMINATE THE ROGRAM:"))
if user_conformation == 1:
    while user_conformation == 1:
        user_input = int(input(menu_option))
        if user_input == 0:
            add_movie()

        elif user_input == 1:
            print(movies)
        elif user_input == 2:
            find_movie()
        elif user_input == 3:
            print("THE PROGRAM TERMINATED.")
        else:
            print("INVALID INPUT PLEASE TRY AGAIN:")

        user_conformation = int(input("TO CONTINUE TYPE 1 OR ENTER 2 TO TERMINATE THE PROGRAM:"))
    else:
        input("Thank You!! come again and have a nice day!! ")
        print("PROGRAM COMPLETED.")
elif user_conformation == 2:
    print("program terminated by the user")
else:
    raise ValueError("Invalid input. please try again..")

"""
test = ["hello"]
test1 = ["hi"]
test2 = []
test2.append(test1)
test2.append(test)
print(test2)
"""