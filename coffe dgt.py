# Demonstrate how to use while loops in and if statements Python
# Author: Ian Gan
# Date: 9/05/2025
# Version 1.0

# While loops
keep_going = "" # The variable contains an empty string
# == is used to check if the variable meets the condition
while keep_going == "":

    like_coffee = input("Do you like coffee? ")

    if like_coffee == "yes":
        print("That is great. I like coffee too!")
        keep_going = "end" # This will end the loop
    if like_coffee == "no":
        print("Fair enough.")
        keep_going = "end"