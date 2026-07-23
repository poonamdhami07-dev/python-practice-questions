#Implement a program that classifies a given angle (input in degrees) into categories such as acute, right, obtuse, or invalid. 
angle = float(input("Enter the angle in degrees: "))

if angle < 0 or angle > 360:
    print("Invalid angle. Please enter an angle between 0 and 360 degrees.")
elif angle < 90:
    print("The angle is acute.")
elif angle == 90:
    print("The angle is right.")
else:
    print("The angle is obtuse.")