#•Start with your program from Exercise 3-4. 
#Add a print() call at the end of your program stating the name of the guest who can’t make it.

#•Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.

#•Print a second set of invitation messages, one for each person who is still in your list.

guests = ["max verstappen","charles leclerc", "lewis hamilton"]
print("{}, you are invited for dinner.".format(guests[0].title()))
print("{}, you are invited for dinner.".format(guests[1].title()))
print("{}, you are invited for dinner.".format(guests[2].title()))

print("\n{} can't make it to dinner.\n".format(guests[0].title()))

#removing guests who cant attend
del(guests[0])

#Adding new guests to replace the removed guests slot in the index of list
guests.insert(0, "carlos sainz")

#print the message again
print("{}, you are invited for dinner.".format(guests[0].title()))
print("{}, you are invited for dinner.".format(guests[1].title()))
print("{}, you are invited for dinner.".format(guests[2].title()))

