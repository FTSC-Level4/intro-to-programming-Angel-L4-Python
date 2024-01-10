
#Dictionary of three major rivers and their country 
rivers = {
    "nile": "egypt",
    "amazon": "brazil",
    "yangtze": "china"
    }

#For loop
#key:value = river:country
#.items() access each of the dictionary's key:value pairs
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

#accessing the keys =river
print("\nThe names of each river included in the dictionary:")
for river in rivers.keys():
    print(f"• {river.title()}")

#accessing the values=country
print("\nThe names of each country included in the dictionary:")
for country in rivers.values():
    print(f"• {country.title()}")