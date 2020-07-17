"""
Project:Make a movie collection app.
    *Debug(program termination)
Author:Devam A
Discreption:
this program take input for movies and makes the list of them and then prints out the list if invalid input is given then it shows error.
this program lacks in saving the data when its finished due to use of list instead of database.
Status:Failed
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
        input("THE PROGRAM COMPLETED.")
    else:
        print("THE PROGRAM TERMINATED.")
elif user_input == 1:
    print("THE PROGRAM TERMINATED.")
else:
    print("INVALID INPUT PLEASE TRY AGAIN:")
