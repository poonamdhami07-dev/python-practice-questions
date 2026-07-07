#Write a Python program that takes a user's age as input and prints whether they are eligible to vote or not (considering the legal voting age is 18). 
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")