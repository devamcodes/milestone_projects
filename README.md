# Milestone Projects:
## Books Library:-
	This is a complete book-collection e-library Application with SQLite Database.
	When the user first runs the program then it will create a databse file which will be encrypted so only using the viewing software the content of the file can be seen.
	Now once the database is created then the program moves forward and asks some basic question about the book that the user wants to add to "MY BOOKS" Wishlist.
	after checking the details of the books (like if the book name already exists in the cart or if the user made any mistake while adding) if there are no errors then,
	the confirmation message is printed now user needs to choose one option from the menu.
	The menu contains 5 option:
		1) Add Book.
		2) View Cart.
		3) Mark the book as read/unread.
		4) Remove Book from list.
		5) Exit the Program.
	2) There are two option for viewing the cart:-
		1> Statement form.
		2> Tabular form.
	3) Mark As read/unread:-
		1> Mark As Read- You need to enter the book name to mark it as read and if there is any error then it will throw an error message and the program starts from the menu options.
		2> Mark As Un-Read- Again you need to enter the book name & the author name and if it matches the name in the databse then it will mark that book as unread otherwise it will throw an error message.
	4)Remove Book From the My Books:-
		Angain you need to eter the name of the book and if it matches the name in the database then it wil remove the book from the list.
	
	Now if the user makes any mistake in between any step then the program crashes and an error message is throw and the program again start from the menu.

## Movie Collection:-
	This is a complete Movie-Collection e-library Application without SQLite Database.
	This application saves the movies in an array.
	When the user firstly runs the program it asks the user to enter the name if user makes any mistake then it will throw an error and restarts the program.
	There are 5 options in the menu:
		1> Add A Movie.
		2> View Movie List.
		3> Find a Particular movie from the list.
		4> Remove a particualr movie from the list.
		5> Exit the program.
	2) View the Movie list:-
	This command will print the array containing movie list.
	
	3) Find the Movie:-
	User needs to enter the movie name and it will check the movie list if the movie is present in the array then it will print it out, otherwise it will throw an error.
	
	4) Remove the movie:-
	The program asks the user to enter the movie name if it matches the name in array then it will remove the movie from the list otherwise it will show an error message.
