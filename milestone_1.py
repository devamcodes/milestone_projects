"""
Project:Make a movie collection app.
    *Debug(program termination)
Author:Devam A
Description:
this program take input for movies and makes the list of them and then prints out the list if invalid input is given then it shows error.
this program lacks in saving the data when its finished due to use of list instead of database.
Status:Failed
"""
user_name = input("PLEASE ENTER YOUR NAME:")
print(f"Hello, {user_name.title()}")

def find_movie(method):
        if method == 1:
            find_movie = input("ENTER MOVIE NAME:")
            for movie in movies:
                if find_movie.title() == elememt.movies.title():
                    print(element)
                    input("PROGRAM COMPLETED.")
                    return movies.index(element)
                
def menu_options():
    menu_options = ['ADD A MOVIE','VIEW THE MOVIE LIST','FIND MOVIE','QUIT PROGRAM']
    for _ in range(len(menu_options)):
        output = print(_, menu_options[_])
    return output
def add_movie():
    user_input_movies = input("PLEASE ENTER A MOVIE NAME:")
    movies.append(user_input_movies)
    user_input = int(input("PLEASE ENTER THE OPTION NUMBER:"))
    output = print("THE MOVIE IS ADDED TO THE COLLECTION.")
    return output

user_conformation = int(input("TO CONTINUE TYPE 8 OR ENTER ANY NUMBER TO TERMINATE:"))

menu_options()

while user_conformation == 8:
    user_input = int(input("PLEASE ENTER THE OPTION NUMBER:"))
    #TODO:afetr this step the program starts malfunctioning.
    movies = []
    
    if user_input == 0:
        while user_input == 0:
                add_movie()
    elif user_input == 1:
         print(movies)
        
    elif user_input == 2:
        print("ENTER MOVIE NAME TO FIND THE MOVIE:")
        find_movie

    elif user_input == 3:
        print("THE PROGRAM TERMINATED.")
        menu_options()
    
    else:
        print("INVALID INPUT PLEASE TRY AGAIN:")
    
else:
    input("PROGRAM COMPLETED.")
