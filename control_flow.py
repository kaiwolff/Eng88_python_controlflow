#Control Flow with if, elif, else

#First let's set up something we check for.

weather = "rainy"

#if the boolean given to an if statement is true, the indented block runs
if weather == "sunny": #remember to use the colon. Also to indent
    print("Enjoy the weather!")

elif weather == "rainy":
    print("Remember to take an umbrella")
else: #this code will run if none of the other options are fulfilled
    #Good practice is to have a contingency should the if statement not activate, so that we can be sure that the code actually ran.
    print("'Something went wrong, input was not recognised")
    #note: a while loop is a better option if we are prompting the user/client/customer for data in a particular format.

#add a condition usign elif if there are several separate conditional cases.