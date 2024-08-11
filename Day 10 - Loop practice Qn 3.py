'''Use a loop to display elements from a given list present at odd index positions'''
# L1 = []
# n = int(input("Enter Number of ELements in The List : "))
# for i in range(n):
#     element = input("Enter ELement " + str(i+1) + " : ")
#     L1.append(element)
# print("Current List : ", L1)
# for i in range(0, len(L1), 2):
#     print(L1[i])




'''Reverse a given integer number'''
# num = int(input("Enter a number: "))
# reverse_number = 0
# print("Given Number ", num)
# while num > 0:
#     digit = num % 10           # Get the last digit
#     reverse_number = reverse_number * 10 + digit  # Add it to the reversed number
#     num = num // 10          # Remove the last digit from the original number
# print("Reverse Number ", reverse_number)




'''Count Vowels in a String'''
# s = input("Enter a string: ")
# vowels = "aeiouAEIOU"
# vowel_count = 0
#
# for char in s:
#     if char in vowels:
#         vowel_count += 1
#
# print(f"Number of vowels in the string: {vowel_count}")




'''Sum of Digits of a Number'''
# n = int(input("Enter A number : "))
# sum_of_digits = 0
# for digit in str(n):
#     sum_of_digits += int(digit)
#
# print(f"The sum of the digits of {n} is {sum_of_digits}.")