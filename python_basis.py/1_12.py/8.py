#Write a program to calculate the sum of all prime numbers within a given range (input by the user). 

start_num = int(input("Enter the starting number: "))
end_num = int(input("Enter the ending number: "))

prime_sum = 0

for num in range(start_num, end_num+ 1):
    if num > 1:  # primes are greater than 1
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_sum += num

print("Sum of prime numbers between", start_num, "and", end_num, "is:", prime_sum)