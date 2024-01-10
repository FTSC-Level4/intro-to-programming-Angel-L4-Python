#function with parameters of size and message for the shirt
def make_shirt(size, message):
    #print statement with the f-string tool
    print(f"\nI will make a {size.title()} sized t-shirt,")
    print(f'with the message "{message.title()}".')

#first call with positional arguments for the parameters
make_shirt("medium", "green viper")

#second call with keyword arguments for the size and message
make_shirt(size="large",message="yellow tiger")