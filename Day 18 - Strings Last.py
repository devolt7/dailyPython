'''Python – Convert Snake case to Pascal case'''
# Snake Case -  where words are written in lowercase and separated by underscores (_). ex: "my_variable_name".
# Pascal Case - where each word in a compound phrase begins with an uppercase letter. ex: "MyVariableName".

# def snake_to_pascal(input_str):
#     result = ""
#     capitalize_next_word = True
#
#     for char in input_str:
#         if char == "_":
#             capitalize_next_word = True
#         elif capitalize_next_word:
#             result += char.upper()
#             capitalize_next_word = False
#         else:
#             result += char
#
#     return result
#
# x = str(input("Enter A Snake Case : "))
# print(snake_to_pascal(x))




'''Check if two strings are Rotationally Equivalent'''
# # Rotationally Equivalent - if one string can be derived from other upon left or right rotation. ek - "Devk" and "vkDe"
# x = str(input("Enter first String : "))
# y = str(input("Enter second String : "))
#
# # printing original strings
# print("The original string 1 is : " + str(x))
# print("The original string 2 is : " + str(y))
#
# res = False
# for idx in range(len(x)):
#     if x[idx: ] + x[ :idx] == y:
#         res = True
#         break
#
# # printing result
# print("Are two strings Rotationally equal ? : " + str(res))




'''convert string to dictionary'''
# str = "Jan = January; Feb = February; Mar = March"
# dictionary = dict(item.split("=") for item in str.split(";"))
# print(dictionary)




'''Remove punctuation from string'''
# import string
#
# def remove_punctuation(input_string):
#     return input_string.translate(str.maketrans('', '', string.punctuation))
#
# # Example usage
# text = "Hello, Doston! kya haa'l hai;n?"
# clean_text = remove_punctuation(text)
# print(clean_text)