'''Factorial'''
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# n = int(input("Enter any number : "))
#
# if n < 0:
#     print("Factorial is not defined for negative numbers.")
# else:
#     print(f"Factorial of {n} is {factorial(n)}")



'''Exponent'''
# def exponent(power, base):
#     if power == 0:
#         return 1
#     else:
#         return base ** power
#
#
# base = int(input("Enter Base : "))
# power = int(input("Enter Power to Raised : "))
# print(f"{base}^{power} = {exponent(power, base)}")




'''Sq Root'''
# def sqrt(n):
#     if n < 0:
#         return "Cannot find square root of a negative number"
#     elif n == 0 or n == 1:
#         return n
#     else:
#         return n ** 0.5
#
# n = int(input("Enter Number for Square Root : "))
# print(f"Square Root of {n} is {sqrt(n)}")

#We can also code these above codes by importing Math module.




'''Dice'''
# import random
# def dice_roll():
#     return random.randint(1,6)
#
# print(dice_roll())