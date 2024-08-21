'''Python | Permutation of a given string using inbuilt function'''
# def generate_permutations(string):
#     if len(string) == 1:
#         return [string]
#
#     permutations = []
#     for i in range(len(string)):
#         fixed_char = string[i]
#         remaining_chars = string[:i] + string[i+1:]
#         for perm in generate_permutations(remaining_chars):
#             permutations.append(fixed_char + perm)
#
#     return permutations
#
# string = str(input("Enter a String : "))
#
# permutations_list = generate_permutations(string)
# z=set(permutations_list)
#
# for perm in z:
#     print(perm)
# No of Combinations of a word in which repetition is possible is n!.
# so, it can be used to check perms.




'''Python | Check for URL in a String'''
# def checkurl(x):
#     url = "https:"
#     if url in x:
#         return "There is URL in - ", x
#     else:
#         return False
#
# q = str(input("Enter a String : "))
# print(checkurl(q))

"""OR"""
# import re
# def Find(string):
#     # findall() has been used
#     # with valid conditions for urls in string
#     regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
#     url = re.findall(regex, string)
#     return [x[0] for x in url]
# string = str(input("Enter a String : "))
# print("Urls: ", Find(string))




'''Python | Word location in String'''
# def find_word_location(string, word):
#     # Find the index of the first occurrence of the word
#     index = string.find(word)
#
#     if index == -1:
#         return f"The word '{word}' was not found in the string."
#     else:
#         return f"The word '{word}' is found at index {index}."
#
# # Input string and word
# input_string = input("Enter a String: ")
# input_word = input("Enter the word to Find: ")
#
# # Find the word location and print the result
# result = find_word_location(input_string, input_word)
# print(result)




'''Convert numeric words to numbers'''
# Python3 code to demonstrate working of
# Convert numeric words to numbers
# Using join() + split()

# help_dict = {
#     'one': '1',
#     'two': '2',
#     'three': '3',
#     'four': '4',
#     'five': '5',
#     'six': '6',
#     'seven': '7',
#     'eight': '8',
#     'nine': '9',
#     'zero': '0'
# }
#
# # initializing string
# test_str = str(input("Enter a String : "))
# # printing original string
# print("The original string is : " + test_str)
# res = ''.join(help_dict[ele] for ele in test_str.split())
#
# # printing result
# print("The string after performing replace : " + res)