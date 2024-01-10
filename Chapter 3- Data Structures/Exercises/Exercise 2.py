#print a message to them. 
#The text of each message should be the same, but each message should be personalized with the person’s name.

Names=["Grizzly", "Panda", "Ice Bear"]

#.format replaces {} which stores the list of names
#indicating the names starting from 0(apple) to 2(kiwi)
print("Hello {}!".format(Names[0]))
print("Hello {}!".format(Names[1]))
print("Hello {}!".format(Names[2]))
