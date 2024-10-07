# Program Name: Lab5.py
# Course: IT1114/Section XXX
# Student Name: Nicole Gonzales
# Assignment Number: Lab#5
# Due Date: 10/05/ 2024
# Purpose: Write a program that will prompt the user for a starting number and an ending number,
# and will print all the prime numbers between the starting number and ending number
# inclusively


#check if num is prime
def is_prime(n):
    if  n < 1:
        return False

    for i in range( 2, int(n ** 0.5) + 1 ):
        if n % i == 0:
            return False
    return True

#input
StartingNum = int(input("Starting Number: "))
EndingNum = int(input("Ending Number: "))

#print prime numbers
for Num in range (StartingNum, EndingNum +1 ):
    if is_prime(Num):
        print(Num)