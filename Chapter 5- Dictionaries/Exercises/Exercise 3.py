#Dictionary of five programming words + five more
glossary = {
    "print": "outputs text or variables to the console.",
    "variables": "stores values or data.",
    "input": "accepts user input from the console.",
    "if statement": "executes code based on a condition.",
    "f-string": "tool for string interpolation and formatting.",
    "for loop":"iterates over a sequence of elements.",
    "while loop": "repeatedly executes code as long as a condition is true.",
    "lists":"ordered collections of items.",
    "dictionaries":"stores key-value pairs.",
    "functions":"blocks of reusable code.",
    "classes": "blueprints for creating objects with properties and methods."
    }

#For loop
#key:value = word:definition
#.items() returns the dictionaries key:value pairs
for word, definition in glossary.items():
    #print with formatted sting to replace and apply each element to coresponding variables
    print(f"\n{word.title()}: \n {definition.title()}")