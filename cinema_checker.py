
while True:

    age = input("\nPlease enter your age. Enter 'exit' to quit the program: ")

    if age == "exit": #this allows the user to quit if they enter 'exit'
        break

    if int(age) >= 18:
        print("You can watch any films we have")
    elif int(age) >=15:
        print("You may watch ratings 15, 12, PG, or U")
    elif int(age) >= 12:
        print("You may watch ratings 12, PG, or U")
    elif int(age) < 12:
        print("You may watch U-rated films, or PG films if you are with a parent")
    else:
        print("Input not recognised, please try again.")

    rating = input("\nPlease enter the age rating of the film you are trying to watch (U, PG, 12, 15, or 18): ")
    can_watch = False #default case is to not allow sale, just in case
    if rating == "U":
        can_watch = True
    if rating == "PG" and int(age) >= 12:
        can_watch = True
    elif rating == "12" and int(age) >= 12:
        can_watch = True
    elif rating == "18" and int(age) >= 18:
        can_watch = True


    #finally, display outcome
    if can_watch:
        print("You can buy this ticket")
        break
    else:
        ("Either you are too young, or you input a rating that does not exist. Please try again")


print("Thank you for using cinema_checker")