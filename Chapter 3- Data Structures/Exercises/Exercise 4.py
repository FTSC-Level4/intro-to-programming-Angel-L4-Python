#If you could invite anyone, living or deceased, to dinner, who would you invite? 
#Make a list that includes at least three people you’d like to invite to dinner. 
#Then use your list to print a message to each person, invitingthem to dinner.

#list of names of the guests
guests = ["max verstappen","charles leclerc", "lewis hamilton"]

#.format is for the names of guests to replace {} in the statement
#index [] of names from 0 to 2 
#.title for capitalization 
print("{}, you are invited for dinner.".format(guests[0].title()))
print("{}, you are invited for dinner.".format(guests[1].title()))
print("{}, you are invited for dinner.".format(guests[2].title()))