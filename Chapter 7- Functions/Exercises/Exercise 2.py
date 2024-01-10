#function that only accept the parameter "title" 
def favorite_book(title):
    #print statement with an f-string for the title
    print(f"One of my favorite books is the {title.title()}.")

#calling the function of the book title inside the argument 
favorite_book("hunger games")