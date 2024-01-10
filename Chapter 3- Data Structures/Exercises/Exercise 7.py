#lists of places 
locations = ["Tokyo", "New York", "Seoul", "Canada", "Paris"]

print("Original order:")
print(locations)


#sorts the list according to its alphabetical order
print("\nAlphabetical:")
print(sorted(locations))
#no changes to the original list
print("Original order:")
print(locations)

#sorts the list according to its reverse alphabetical order, using a true reverse parameter
print("\nReverse alphabetical:")
print(sorted(locations, reverse=True))
#no changes to the original list
print("Original order:")
print(locations)


#reverses the list according from the last to the first, using a reverse method
print("\nReversed:")
locations.reverse()
print(locations)
#changes the original list
print("Original order:")
print(locations)


#reverses the list again according from the first to the last, using the reverse method
print("\nOriginal order:")
locations.reverse()
print(locations)
#changes back to the original list
print("Original order:")
print(locations)


#sorts the list according to its alphabetical order, using a sort method
print("\nAlphabetical")
locations.sort()
print(locations)
#changes the original list
print("Original order:")
print(locations)


#sorts the list according to its reverse alphabetical order, using a  sort method and true reverse parameter
print("\nReverse alphabetical")
locations.sort(reverse=True)
print(locations)
#changes the original list
print("Original order:")
print(locations)