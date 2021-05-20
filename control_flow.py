#Control Flow with if, elif, else

#First let's set up something we check for.

weather = "rainy"

#if the boolean given to an if statement is true, the indented block runs
if weather == "sunny": #remember to use the colon. Also to indent
    print("Enjoy the weather!")

elif weather == "rainy":#this will run shoudl the if statement not be true, but another set of conditions is fulfilled
    print("Remember to take an umbrella")
    #can have as many statements as we want. Cna also nest if statements, or have several conditions for one statement
else: #this code will run if none of the other options are fulfilled
    #Good practice is to have a contingency should the if statement not activate, so that we can be sure that the code actually ran.
    print("'Something went wrong, input was not recognised")
    #note: a while loop is a better option if we are prompting the user/client/customer for data in a particular format.
    #havign several if statements in sequence will executed
    #Havign several "if" blocks will check each conditions, elif will only be checked

#as an example, age restrictions on cinema tickets. See cinema_checker.py


