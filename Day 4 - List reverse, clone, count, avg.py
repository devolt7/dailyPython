'''Reversing List methods'''
#M-1
# L1 = []
# n = int(input("Enter Number of ELements in The List : "))
# for i in range(n):
#     element = input("Enter ELement " + str(i+1) + " : ")
#     L1.append(element)
# print("Current List : ", L1)
#
# # Reversing the List
# L1.reverse()
# print("List After Reversing : ", L1)

#M-2
# def Rev(element):
#     return element[::-1]
#
# L1 = []
# n = int(input("Enter Number of ELements in The List : "))
# for i in range(n):
#     element = input("Enter ELement " + str(i+1) + " : ")
#     L1.append(element)
# print("Current List : ", L1)
# print("Reversed List : ", Rev(L1))


'''Cloning A List : '''
#M-1
# L1 = []
# n = int(input("Enter Number of ELements in The List : "))
# for i in range(n):
#     element = input("Enter ELement " + str(i+1) + " : ")
#     L1.append(element)
# print("Current List : ", L1)
#
# # Cloning the List
# L2 = L1[:]
# print("Cloned List : ", L2)

#M-2
# Python code to clone or copy a list
# Using the in-built function extend()
# def Cloning(li1):
#     li_copy = []
#     li_copy.extend(li1)
#     return li_copy
#
# # Driver Code
# li1 = [4, 8, 2, 10, 15, 18]
# li2 = Cloning(li1)
# print("Original List:", li1)
# print("After Cloning:", li2)

#M-3
#Using Assignment Operator
# def clone(L1):
#     L2 = L1
#     return L2
# L1 = []
# n = int(input("Enter Number of ELements in The List : "))
# for i in range(n):
#     element = input("Enter ELement " + str(i+1) + " : ")
#     L1.append(element)
# L2 = clone(L1)
# print("Current List : ", L1)
# print("Cloned List : ", L2)

#M-3 We can also do this by using Copy method by importing copy.




'''Count Occurrences of an Element in a List'''
# def count(list):
#     element = input("Enter the element to count : ")
#     count = list.count(element)
#     return count
#
# L1 = []
# n = int(input("Enter Number of ELements in The List : "))
# for i in range(n):
#     element = input("Enter Element " + str(i+1) + " : ")
#     L1.append(element)
#
# print("Occurrences of element : ", count(L1))







'''To find average of elements in a List'''
# def avg(x):
#     if len(x) == 0:
#         return 0
#     return sum(x) / len(x)
#
# L1 = []
# n = int(input("Enter Number of Elements in The List : "))
# for i in range(n):
# # Conversion to float is very very important
#     element = float(input("Enter Element " + str(i+1) + " : "))
#     L1.append(element)
# print(f"Current List : ", L1)
# average = avg(L1)
# print("The Average of elements in the list is : ", average)