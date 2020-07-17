"""
Project:Make a movie collection app.
Directions:-
    
    2)make list of movies.->Done
    3) create a menu. ->Done
    4)Ask for comformation on the selection in menu_option->Done
    5)Debug(program termination)
Author:Devam A
Discreption:

"""
user_name = input("PLEASE ENTER YOUR NAME:")
print(f"Hello, {user_name.title()}")
menu_options = ['ADD A MOVIE','QUIT THE PROGRAM']
for _ in range(len(menu_options)):
    print(_, menu_options[_])
user_input = int(input("PLEASE ENTER CORRESPONDING NUMBER:"))
movies = []
if user_input == 0:
    user_conformation = int(input("TO CONFORM ADDING THE MOVIE TYPE 8 OR ENTER ANY NUMBER"))
    if user_conformation == 8:
        while user_conformation == 8:
            user_input_movies = input("PLEASE ENTER A MOVIE NAME:")
            movies.append(user_input_movies)
            user_conformation = int(input("ENTER 8 TO CONTINUE ADDING OR ENTER ANY NUMBER TO VIEW MOVIE-LIST:"))
        print(movies)
    else:
        print("THE PROGRAM TERMINATED.")
        
else:
    print("INVALID INPUT PLEASE TRY AGAIN:")
input("THE PROGRAM COMPLETED.")
