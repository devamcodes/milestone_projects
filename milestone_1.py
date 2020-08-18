"""
Project:Movie collection app.
Author:Devam A

Description:
**This program needs database.


Status:SUCCESSFUL

changes to be made:
1. after the error message goes on the program should continue.
"""
def enter_user_name():
    user_name = input("PLEASE ENTER YOUR NAME:")
    user_name_booleane = bool(user_name)
    if user_name_booleane == True:
        print(f"Hello, {user_name.title()}")
    else:
        print("program terminated!!")
        raise ValueError("Invalid input please enter a valid name")



movies = []
find_movie_name = []


def find_movie_option():
    #some statements changed to coorect the grammar.
    find_movie = input("ENTER MOVIE NAME:")
    if find_movie in movies:
        print(f"BOOYA!!!We have found the {find_movie.title()} movie in your movie collection")
    else:
        raise ValueError("THIS MOVIE IS NOT IN YOUR COLLECTION,TRY AGAIN!")

#TODO:after raising the error the program must continue but still it is not happening after the use of that keyword.


#TODO:remove movie option remaining.
menu_option = """
Please enter the option number:
  1. Add Movie
  2. View MovieList
  3. Find Movie
  4. Remove Movie
  5. Exit Program
-->"""

def add_movie():
    
    user_input_movies = input("PLEASE ENTER A MOVIE NAME:")
    movies.append(user_input_movies)
    print("THE MOVIE IS ADDED TO THE COLLECTION.")



def remove_movie():
    user_input_movie_name = input("enter the movie name you want to remove:")
    if user_input_movie_name in movies:
        print(f"we have removed  '{user_input_movie_name}' movie from your movie collection.")
    else:
        print(f"we are unable to find the movie in your movie collection...")
        raise ValueError("please enter the correct movie name.")


enter_user_name()
user_input = 0#due to this user conformation part can be removed.
if user_input == 0:
    while user_input == 0:
        #TODO:if enter is pressed instead of any number then raise an error.
        user_input = int(input(menu_option))
        #TODO:if enter is pressed without any value then error should raise and loop should continue.
        if user_input == 1:
            add_movie()
        elif user_input == 2:
            print(movies)
        elif user_input == 3:
            find_movie_option()
        elif user_input == 4:#option added
            remove_movie()
        elif user_input == 5:
            print("program completed...")
            break
        else:
            raise ValueError("Invalid Input!! try again...")
        user_input = 0

else:
    raise ValueError("Invalid input. please try again..")
