#apply the math equation of pi (accessing from math and imporing the function of pi)
from math import pi

#generating a "ask user for radius" using the variable "Radius" 
#with the value the data type "float" and the input function
Radius = float(input ("Radius of the circle: "))

#output displays the "Radius" and its area as a string data type 
#with imported math equation of pi, it can calculate for the area with any given radius 
print ("The area of the circle with radius " + str(Radius) + " is: " + str(pi * Radius**2))
