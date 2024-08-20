'''Find words which are greater than given length k in python'''
# def find_long_words(words, k):
#     return [word for word in words if len(word) > k]


# words = []
# elements = int(input("Enter Number of words : "))
# for i in range(elements):
#     word = input("Enter word " + str(i+1) + " : ")
#     words.append(word)
# k = int(input("Enter Length : "))
# long_words = find_long_words(words, k)
# print(long_words)




'''Python program for removing i-th character from a string'''
# def remove(string, i):
#     # Slice the string to exclude the i-th character
#     return string[:i] + string[i+1:]
#
# x = str(input("Enter a String : "))
# y = int(input("Enter Index To Remove : "))
# print(remove(x, y))




'''Python program to find uncommon words from two Strings'''
# def find_uncommon_words(str1, str2):
#     # Split both strings into words
#     words1 = set(str1.split())
#     words2 = set(str2.split())
#
#     # Find words that are in one set but not the other (symmetric difference)
#     uncommon_words = words1.symmetric_difference(words2)
#
#     return list(uncommon_words)
#
# # Input strings
# str1 = input("Enter the first string: ")
# str2 = input("Enter the second string: ")
#
# # Find and print uncommon words
# uncommon = find_uncommon_words(str1, str2)
# print("Uncommon words:", uncommon)




'''Swap commas and dots in a String'''
# def swap_commas_dots(string):
#     # Replace commas with a temporary placeholder
#     temp_string = string.replace(',', '<comma>')
#
#     # Replace dots with commas
#     temp_string = temp_string.replace('.', ',')
#
#     # Replace the temporary placeholder with dots
#     swapped_string = temp_string.replace('<comma>', '.')
#
#     return swapped_string
#
# # Input string
# input_string = input("Enter a string : ")
#
# # Perform the swap and print the result
# result = swap_commas_dots(input_string)
# print("Modified string : ", result)