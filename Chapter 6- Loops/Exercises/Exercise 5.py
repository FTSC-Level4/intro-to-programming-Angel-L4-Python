#Using the list sandwich_orders from Exercise 7-8, 
#make sure the sandwich 'pastrami' appears in the list at least three times. 
#Add codenear the beginning of your program to print a message saying the deli has run out of pastrami, 
#and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. 
#Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = ["pastrami", "egg", "ham", "pastrami", "bacon", "avocado", "cheese", "pastrami"]
finished_sandwiches = []
print(f"Sandwich Orders: {sandwich_orders}\n"
      f"Finished Sandwiches: {finished_sandwiches}\n"
      )

#statement saying the deli has run out of pastrami
print("I'm sorry, we are out of pastrami.")
#While loop
#accessing "pastarami" from the list of sandwich_orders
while "pastrami" in sandwich_orders:
    #removing "pastarami" from the list
    sandwich_orders.remove('pastrami')

print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I am making {} sandwich.".format(current_sandwich.title()))
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I made a {} sandwich.".format(sandwich.title()))

print(f"\nSandwich Orders: {sandwich_orders}\n"
      f"Finished Sandwiches: {finished_sandwiches}"
      )