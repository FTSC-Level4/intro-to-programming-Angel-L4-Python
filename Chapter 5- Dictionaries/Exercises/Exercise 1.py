#Use a dictionary to store information about a person you know.
#Store their first name, last name, age, and the city in which they live. 
#You should have keys such as first_name, last_name, age, and city. 
#Print each piece of information stored in your dictionary.

#Dictionary of information about a person
#variable "person"
person = {
  "first_name": "alvin",
  "last_name": "javier",
  "age": "22",
  "city": "pangasinan",
}

#printing the variable with the name of each keys to access its value
print("First Name:",person['first_name'].title())
print("Last Name:", person['last_name'].title())
print("Age:", person['age'].title())
print("City:", person['city'].title())