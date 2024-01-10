
#empty pets list
pets = []

#1st pet
pet1 = {
    "animal breed": "persian cat",
    "pet name": "chantel",
    "owner name": "angel"
}
#insert pet1 to the empty pets list under the index of 0
pets.insert(0,pet1)

#2nd pet
pet2 = {
    "animal breed": "corgi dog",
    "pet name": "cookie",
    "owner name": "alvin"
}
#insert pet2 to the empty pets list under the index of 1
pets.insert(1,pet2)

#3rd pet
pet3 = {
    "animal breed": "mini lop bunny",
    "pet name": "hop",
    "owner name": "alice"
}
#append pet3 last to the empty pets list
pets.append(pet3)

#For loop
#new variable "pet" = pets list
for pet in pets:
    #f "formatted sting" transforms the assigned variable to its value
    print(f"\nMy information about {pet['pet name'].title()}:")

    #for loop
    #dictionary variables "key, value" in the pet list
    #.items() access each of the dictionary's key:value pairs
    for key, value in pet.items():
        print(f"\t{key}: {value}".title())