#Develop a program that takes numbers as input and calculates the sum until it encounters a negative number, using the break statement. 

total = 0
while True:
    num = int(input("Enter a number: "))
    if num < 0:   # stop if negative number
        break
    total += num

print("The sum of entered numbers is:", total)