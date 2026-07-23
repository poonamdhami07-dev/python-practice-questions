#Write a Python program that calculates the factorial of a given number using a loop. Take the number as input.| 

num = int(input("Enter a number: "))

factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("Factorial of", num, "is:", factorial)

