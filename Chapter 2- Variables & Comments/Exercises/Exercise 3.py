#\t(tab space), \n(next line)
Name="ANGELA"
print(Name,"\n")

#"str_NAME" as the variable for the "Name" with ".lstrip()" function to identify the whitespace/character
#lstring removes the leading whitespace/character
str_NAME = Name.lstrip("A")
print("Name.lstrip()", "\t \n", str_NAME)

#rstring removes the Trailing whitespace/character
str_NAME = Name.rstrip("A")
print("\nName.rstrip()", "\t \n", str_NAME)

#string removes the all the specified whitespace/character
str_NAME = Name.strip("A")
print("\nName.strip()", "\t \n", str_NAME)