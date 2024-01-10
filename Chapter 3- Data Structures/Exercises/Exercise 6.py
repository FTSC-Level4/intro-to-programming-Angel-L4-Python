guests = ["max verstappen","charles leclerc", "lewis hamilton"]
print("{}, you are invited for dinner.".format(guests[0].title()))
print("{}, you are invited for dinner.".format(guests[1].title()))
print("{}, you are invited for dinner.".format(guests[2].title()))

print("\n{} can't make it to dinner.\n".format(guests[0].title()))

del(guests[0])
guests.insert(0, "carlos sainz")
print("{}, you are invited for dinner.".format(guests[0].title()))
print("{}, you are invited for dinner.".format(guests[1].title()))
print("{}, you are invited for dinner.".format(guests[2].title()))

#inviting more guest for the bigger table
print("\nWe got a bigger table.")
#.insert new guests for the list under the index of 3,4,and .append the last index 5
guests.insert(3, "lando norris")
guests.insert(4, "yuki tsunoda")
guests.append("george russell")
print("\n", guests)

print("{}, you are invited for dinner.".format(guests[3].title()))
print("{}, you are invited for dinner.".format(guests[4].title()))
print("{}, you are invited for dinner.".format(guests[5].title()))

#table wouldn't be able to arrive on time
print("\nSorry, we can only invite two people to dinner. \n")

print("Sorry, {} there's no room at the table.".format(guests[2].title()))
print("Sorry, {} there's no room at the table.".format(guests[3].title()))
print("Sorry, {} there's no room at the table.".format(guests[4].title()))
print("Sorry, {} there's no room at the table.".format(guests[5].title()))

#removing the guests 
guests.pop()
guests.pop()
guests.pop()
guests.pop()

print("\n")
print(guests)

#clearing the list of guests 
guests.clear()
print(guests)