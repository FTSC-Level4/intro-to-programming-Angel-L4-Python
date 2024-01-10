#Make a list called sandwich_orders and fill it with the names of various sandwiches. 
#Then make an empty list called finished_sandwiches.
#Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. 
# As each sandwich is made,move it to the list of finished sandwiches. 
# After all the sandwiches have been made, print a message listing each sandwich that was made.

#list filled with various sandwiches names
sandwich_orders = ["egg", "ham", "bacon", "avocado", "cheese"]
#empty list
finished_sandwiches = []
print(f"Sandwich Orders: {sandwich_orders}\n"
      f"Finished Sandwiches: {finished_sandwiches}\n"
      )

#while loop
while sandwich_orders:
    #removed names from sandwich_orders would be transfered to a new list called current_sandwich, 
    #which would temporary hold the removed values to be accessed again later 
    current_sandwich = sandwich_orders.pop()
    print("I am making {} sandwich.".format(current_sandwich.title()))
    #current_sandwich list will add its values to the empty list called finished_sandwich
    finished_sandwiches.append(current_sandwich)

print("\n")
#For loop
#new variable "sandwich" for finished_sandwich list
for sandwich in finished_sandwiches:
    print("I made a {} sandwich.".format(sandwich.title()))

print(f"\nSandwich Orders: {sandwich_orders}\n"
      f"Finished Sandwiches: {finished_sandwiches}"
      )