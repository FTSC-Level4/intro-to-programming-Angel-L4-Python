#function with parameters and arguments of size and message for the shirt
def make_shirt(size="large",message="I love Python"):
    print(f"\nI will make a {size.title()} sized t-shirt,")
    print(f"with the message '{message.title()}'.")

#large shirt and a medium shirt with the default message
make_shirt()
make_shirt(size="medium")

#a shirt of any size with a different message.
make_shirt("small", "I love Javascript")