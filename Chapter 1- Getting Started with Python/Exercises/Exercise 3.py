#import the datetime from the system of the device
import datetime

#"now" as the variable with the value of the imported "datetime" 
#along with (datetime.now()) function to get the current date and time
now=datetime.datetime.now()
print("Current Date and Time:")

#the variable "now" and the "strftime"or(datetime.now()) is to format the "datetime" data in a string.
print(now.strftime("%d/%m/%Y, %H:%M:%S"))

