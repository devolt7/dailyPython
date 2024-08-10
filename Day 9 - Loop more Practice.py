'''Use else block to display a message “Done” after successful execution of for loop'''
# for i in range(1,8):
#     print(i)
# else:
#     print("Done!")




'''Write a program to display all prime numbers within a range'''
# #A prime number is a number that can only be divided by itself and 1 without remainders.
# def is_prime(min, max):
#     for num in range(min, max + 1):
#         if num > 1:
#             for i in range(2, num):
#                 if (num % i) == 0:
#                     break
#             else:
#                 print(num)
#
# min = int(input("Enter Starting Number : "))
# max = int(input("Enter Ending Number : "))
# is_prime(min, max)




'''Display Fibonacci series up to n terms'''
# Function to display Fibonacci series up to n terms
# def fibonacci_series(n):
#     a, b = 0, 1
#     for i in range(n):
#         print(a, end=' ')
#         a, b = b, a + b
#
# # Number of terms
# n = int(input("Enter Number of Terms Fibonacci series to print : "))
# fibonacci_series(n)




'''Find the factorial of a given number using Loop'''
#def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
#
# n = int(input("Enter a Number: "))
# print(f"The factorial of {n} is {factorial(n)}")