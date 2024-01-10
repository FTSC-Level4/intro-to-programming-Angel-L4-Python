#a programme that calculates how many USB sticks she can buy and how many pounds she will have left
#use the arithmetic operators (/dvide,*multiply,-subtract)

#A girl heads to a computer shop to buy some USB sticks. 
#She loves USB sticks and wants as many as she can get for £50. They are £6 each.
#Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.

USBstick=6
Money=50

#divide 50(USBStick) by 6(Wants) to get the number of USB Sticks she can buy
x=Money/USBstick
#convert the answer (that may result to a decimal) into a whole number (integer)
#X=int(x)

#multiply the answer (of how many USB Sticks she can buy) to the cost of each USB Sticks
y=x*USBstick
#Y=int(y)

#then subtract the total cost of all the USB Sticks she can buy to 50
z=Money-y
#Z=int(z)

print("She can buy","%.2f" %x,"USB sticks and she will have","%.2f" %z,"pounds left.")