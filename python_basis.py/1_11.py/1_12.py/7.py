# Develop a program that prints the Fibonacci sequence up to a certain number of terms. Allow the user to input the number of terms.

n_terms = int(input("Enter the number of terms: "))
#first two numbers
a,b = 0,1

print("Fibonacci Series: ")

for i in range(n_terms):
    print(a,end=" ")
    a, b = b, a + b