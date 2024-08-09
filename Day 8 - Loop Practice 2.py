'''program to display only those numbers from a list that satisfy the following conditions :
The number must be divisible by five
If the number is greater than 150, then skip it and move to the next number
If the number is greater than 500, then stop the loop'''
# numbers = [100, 151, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]
# for num in numbers:
#     if num % 5 == 0 and num <= 150:
#         print(num)
#     elif num > 500:
#         break




'''Count the total number of digits in a number using While Loop'''
# num = int(input("Enter any Number : "))
# count = 0
# while num != 0:
#     # floor division to reduce the last digit from number
#     num = num // 10
#
#     # increment counter by 1
#     count = count + 1
# print("Total Digits are:", count)




'''Print list in reverse order using a loop'''
# L1 = []
# n = int(input("Enter Number of ELements in The List : "))
# for i in range(n):
#     element = input("Enter ELement " + str(i+1) + " : ")
#     L1.append(element)
# print("Current List : ", L1)
# # Loop to print list in reverse order
# # len(list1) -1: because index start with 0
# # iterate list in reverse order
# # star from last item to first which is "size" so it's starting index
# size = len(L1) - 1
# for i in range(size, -1, -1):
#     print(L1[i])




'''Display numbers from -10 to -1 using for loop'''
# for i in range(-10, 0, 1):
#     print(i)