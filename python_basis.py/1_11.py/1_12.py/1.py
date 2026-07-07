#Write a Python program that takes a number as input and determines whether it is positive, negative, or zero. Use if, else, and elif statements for decision-making. 
number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")