#Implement a program that prints the multiplication table for a given number. Allow the user to input the number. 

num = int(input("Enter the mutlpication table number: "))
for i in range (1,11):
    print(num,"X",i,"=",num*i)
else: 
    print("Invalid choice. Check the input.")