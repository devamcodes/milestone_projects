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
try:
    user_input = int(input(menu_option))
    while user_input != 5:
            #TODO:if enter is pressed instead of any number then raise an error.

            #TODO:if enter is pressed without any value then error should raise and loop should continue.
        try:
            if user_input == 1:
                add_movie()
            elif user_input == 2:
                print(movies)
            elif user_input == 3:
                find_movie_option()
            elif user_input == 4:
                remove_movie()
            else:
                print("Error occurred...")
                input("Press any to run the program again.")
                user_input = int(input(menu_option))

        except:
            input("Invalid Input!! try again...")
            user_input = int(input(menu_option))

except:
    input("Error occurred while getting the input pls try with the valid input. press any key to continue.")
    try:
        user_input = int(input(menu_option))
        while user_input != 5:
            # TODO:if enter is pressed instead of any number then raise an error.

            # TODO:if enter is pressed without any value then error should raise and loop should continue.
            try:
                if user_input == 1:
                    add_movie()
                elif user_input == 2:
                    print(movies)
                elif user_input == 3:
                    find_movie_option()
                elif user_input == 4:
                    remove_movie()
                else:
                    print("Error occurred...")
                    input("Press any to run the program again.")
                    user_input = int(input(menu_option))

            except:
                print("Invalid Input!! try again...")
                user_input = int(input(menu_option))


    except:
        raise ValueError("Multiple Invalid inputs!!! Please try again by run the program from the start...")

