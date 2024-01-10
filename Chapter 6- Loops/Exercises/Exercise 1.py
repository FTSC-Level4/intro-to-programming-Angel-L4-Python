#Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. 
#As they enter each topping, print a message saying you’ll add that topping to their pizza.

#while loop with true statment
while True:
    #string data type for user input
    toppings = str(input("What kind of pizza topping would you like?: "))
    print("Enter 'Done' or 'done' to finish.")
    #break statement when user inputs "Done"
    if toppings == "Done" or toppings == "done":
        break
    #f to insert user's input in print statement
    #.title for the capitalization of the user's input
    print(f"\nI will add {toppings.title()} to your pizza!\n")