'''Python program to print all odd numbers in a range'''
# start = int(input("Enter the start of the range : "))
# end = int(input("Enter the end of the range : "))
#
# L = []
# for num in range(start, end+1):
#     if num % 2 != 0:
#         L.append(num)
#
# print(f"{L}\nNumber of Odd Numbers Between {start} and {end} is :", len(L))




'''Python program to print positive numbers in a list'''
# L1 = []
# n = int(input("Enter Number of Elements in The List : "))
# for i in range(n):
#     element = int(input("Enter Element " + str(i+1) + " : "))
#     L1.append(element)
# print("Current List : ", L1)
#
# L2 = []
# for num in L1:
#     if num > 0:
#         L2.append(num)
#
# if len(L2) == 0:
#     print("No Positive Numbers in the List")
# else:
#     print("Positive Numbers in the List : ", L2)
#     print("Number of Positive Numbers in the List : ", len(L2))




'''To print Duplicates from a list of integers'''
# def duplicate_list(y):
#     duplicates = set([x for x in y if y.count(x) > 1])
#     #creating a set becuase set cannot take duplicate values.
#     return duplicates
#
# L1 = []
# n = int(input("Enter Number of Elements in The List : "))
# for i in range(n):
#     element = int(input("Enter Element " + str(i+1) + " : "))
#     L1.append(element)
# print("Current List : ", L1)
# print("Set of Duplicate Elements in the List is :", duplicate_list(L1))




'''To print Uniques from a list of Integers'''
# def unique_list(x):
#     # Extracting elements that occur exactly once
#     unique = {num for num in x if x.count(num) == 1}
#     return unique
#
# L1 = []
# n = int(input("Enter Number of Elements in The List : "))
# for i in range(n):
#     element = int(input("Enter Element " + str(i+1) + " : "))
#     L1.append(element)
# print("Current List : ", L1)
# print("Set of Unique Elements in the List is :", unique_list(L1))