#A Python dictionary can be used to model an actual dictionary. 
#However, to avoid confusion, let’s call it a glossary.
#* Think of five programming words you’ve learned about in the previous chapters. 
#Use these words as the keys in your glossary, and store their meanings as values.
#* Print each word and its meaning as neatly formatted output. 
#You might print the word followed by a colon and then its meaning, 
#or print the word on one line and then print its meaning indented on a second line. 
#Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

#Dictionary of five programming words
glossary = {
    "print": "outputs text or variables to the console.",
    "variables": "stores values or data.",
    "input": "accepts user input from the console.",
    "if statement": "executes code based on a condition.",
    "f-string": "tool for string interpolation and formatting."
    }

#variable name for the keys to be accessed each
word = "print"
#print with formatted sting to replace and apply each element to coresponding variables:
#variable name "word", key:value "word:definition", and capitalization ".title()"
print(f"\n{word.title()}: \n {glossary[word].title()}")


word = "variables"
print(f"\n{word.title()}: \n {glossary[word].title()}")

word = "input"
print(f"\n{word.title()}: \n {glossary[word].title()}")

word = "if statement"
print(f"\n{word.title()}: \n {glossary[word].title()}")

word = "f-string"
print(f"\n{word.title()}: \n {glossary[word].title()}")