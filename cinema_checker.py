
while True:

    age = input("\nPlease enter your age. Enter 'exit' to quit the program: ")

    #checking if wanting to exit, or restarting if input not recognised.
    if age.isdigit() != True:
        if age == "exit": #this allows the user to quit if they enter 'exit'
            break
        else:
            print("Input not recognised, please try again")
            continue

    if int(age) >= 18:
        print("You can watch any films we have")
    elif int(age) >=15:
        print("You may watch ratings 15, 12, PG, or U")
    elif int(age) >= 12:
        print("You may watch ratings 12, PG, or U")
    elif int(age) < 12:
        print("You may watch U-rated films, or PG films if you are with a parent")

    rating = input("\nPlease enter the age rating of the film you are trying to watch (U, PG, 12, 15, or 18): ")

    can_watch = False  # default case is to not allow sale, just in case
    if rating.isdigit() or rating == "U" or rating == "PG":

        if rating == "U":
            can_watch = True
        if rating == "PG" and int(age) >= 12:
            can_watch = True
        elif rating == "12" and int(age) >= 12:
            can_watch = True
        elif int(age) >= 18:
            can_watch = True
    else:
        print("The input for rating was not recognised. Please try again")
        continue


    #finally, display outcome
    if can_watch:
        print("You can buy this ticket")
        break
    else:
        print("You may, unfortunately, not watch this movie.")
        break

print("Thank you for using cinema_checker")