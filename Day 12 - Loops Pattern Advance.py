'''Full Pyramid Patterns in Python using Loop'''
# n = int(input("Enter Height of Full Pyramid : "))
# for i in range(1, n + 1):
#     # Print leading spaces
#     for j in range(n - i):
#         print(" ", end="")
#
#     # Print asterisks for the current row
#     for k in range(1, 2*i):
#         print("*", end="")
#     print(" ")




'''Pyramid Patterns in Python with Alphabet'''
# n = int(input("Enter Height of Pyramid Pattern : "))
# # Initializing alph = 65 as A takes value 65 in ASCII
# alph = 65
# for i in range(0, n):
#     print(" " * (n-i), end=" ")
#     for j in range(0, i+1):
#         print(chr(alph), end=" ") # The chr() function is used to convert ASCII values back to characters.
#         alph += 1
#     alph = 65
#     print()




'''Hill Pattern'''
# n = int(input("Enter Height for Hill Pattern : "))
# for i in range(n):
#     for j in range(0, n-i):
#         print(" ", end = " ")
#     for j in range(i):
#         print("*", end = " ")
#     for j in range(0, i+1):
#         print("*", end = " ")
#     print(" ")




'''Reverse Hill'''
# n = int(input("Enter Height for Hill Pattern : "))
# for i in range(n):
#     for j in range(i+1):
#         print(" ", end = " ")
#     for j in range(i, n-1):
#         print("*", end = " ")
#     for j in range(i, n):
#         print("*", end = " ")
#     print(" ")




'''To Print a Diamond Pattern'''
# # Just Place Hill Pattern Above Reverse Hill Pattern
# n = int(input("Enter Size of Diamond Pattern : "))
# for i in range(n-1):
#     for j in range(0, n-i):
#         print(" ", end = " ")
#     for j in range(i):
#         print("*", end = " ")
#     for j in range(0, i+1):
#         print("*", end = " ")
#     print(" ")
# for i in range(n):
#     for j in range(i+1):
#         print(" ", end = " ")
#     for j in range(i, n-1):
#         print("*", end = " ")
#     for j in range(i, n):
#         print("*", end = " ")
#     print(" ")