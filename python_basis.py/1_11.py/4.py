#Develop a Python script that calculates and prints the result of raising a user-input base to a user-input exponent without using the ** operator.
base = float(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
result = 1
for i in range(exponent):
    result *= base
print("The result of", base, "raised to the power of", exponent, "is:", result)