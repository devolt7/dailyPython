'''Summation of List Elements'''
# def summ(x):
#     return sum(x)
# L1 = []
# n = int(input("Enter Number of Elements in The List : "))
# for i in range(n):
#     element = int(input("Enter Element " + str(i+1) + " : "))
#     L1.append(element)
# print("Current List : ", L1)
# print("Sum of List Elements : ", summ(L1))
## IMPORTANT - In the above code i created a user defined function named "summ" instead of using "sum" using "sum" will give an error becuase it's already a built in function so can't be created again by the programmer.




'''Multiple of List Elements'''
# def mult(x):
#     result = 1
#     for i in x:
#         result = result * i
#     return result
# L1 = []
# n = int(input("Enter Number of Elements in The List : "))
# for i in range(n):
#     element = int(input("Enter Element " + str(i+1) + " : "))
#     L1.append(element)
# print("Current List : ", L1)
# print("Multiple of List Elements : ", mult(L1))




''' 2nd Largest Number from List'''
# def second_largest(x):
#     x.sort()
#     return x[-2]
# L1 = []
# n = int(input("Enter Number of Elements in The List : "))
# for i in range(n):
#     element = int(input("Enter Element " + str(i+1) + " : "))
#     L1.append(element)
# print("Current List : ", L1)
# print("Second Largest Element of the List : ", second_largest(L1))
# # The thing to remember that "sort()" sorts the given list in ascending order so largest element is on the last place and second largest is on second last place.




'''To print Number of Even Numbers in list'''
# def sumeven(x):
#     L2 = []
#     for i in x:
#         if i % 2 == 0:
#             L2.append(i)
#     return len(L2)
#
# L1 = []
# n = int(input("Enter Number of Elements in The List : "))
# for i in range(n):
#     element = int(input("Enter Element " + str(i+1) + " : "))
#     L1.append(element)
# print("Current List : ", L1)
# print(f"Number of Even Numbers in the Given List : ", sumeven(L1))
# #To print those Even numbers :
# for num in L1:
#     # checking condition
#     if num % 2 == 0:
#         print(num, end=" ")
