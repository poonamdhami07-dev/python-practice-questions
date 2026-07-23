# Write a program that coefficients of a quadratic equations as input and solves for the roots. Handle both real and complex roots.
import cmath
#quadratic_eq : ax**2 + bz + c = 0

a = float(input("Enter a : "))
b = float(input("Enter b : "))
c = float(input("Enter c : "))

discriminant = b**2 - 4*a*c
root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
root2 = (-b - cmath.sqrt(discriminant)) / (2*a) 
print("Root 1: ",root1)
print("Root 2: ",root2)

