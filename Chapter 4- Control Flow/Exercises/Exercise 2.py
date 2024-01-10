
#•If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
#•If the alien’s color isn’t green, print a statement that the player just earned 10 points.
#Write one version of this program that runs the if block and another that runs the else block.

#version1
alien_color='Green'
print("Version 1 (Green)")

if alien_color=='Green':
    print("You have earned 5 points!\n")

else:
    print("You just earned 10 points!\n")

#version2
alien_color='Yellow'
print("Version 2 (Yellow)")

if alien_color=='Green':
    print("You have earned 5 points!\n")

else:
    print("You just earned 10 points!\n")