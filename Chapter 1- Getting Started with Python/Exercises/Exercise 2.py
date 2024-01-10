#to print the current version of python of a device

#import function with platform (can access the operating system informations of a device)
import platform

print("Python Version")
#function "python_version()" to access the python version of a device 
#while using "()" as string 'major.minor.patchlevel'
print(platform.python_version())

