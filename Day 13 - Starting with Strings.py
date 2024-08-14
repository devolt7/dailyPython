'''Python program to check whether the string is Symmetrical or Palindrome'''
# def is_Palindrome(x):
#     rev = x[::-1]
#     if (x == rev):
#         return f"{x} is a Palindrome"
#     else:
#         return f"{x} is not a Palindrome"
#
# def is_symmetrical(s):
#     mid = len(s) // 2
#     if s[:mid] == s[-mid:]:
#         return f"{s} is also Symmetrical"
#     else:
#         return f"{s} is not Symmetrical"
#
# stree = str(input("Enter a String : "))
# print(is_Palindrome(stree))
# print(is_symmetrical(stree))




'''To Remove Letters From a String in Python'''
# string = str(input("Enter a String : "))
# print(string)
# letters_to_remove = str(input("Enter Letter to Remove from entire String : "))
#
# # Create a translation table
# translator = str.maketrans("", "", letters_to_remove)
#
# # Remove letters
# result = string.translate(translator)
# # Yaha translation table se "letter_to_remove" ki jgah ("") mtlb kuch bhi nhi add hojayega.
# print(result)




'''Python program to print even length words in a string'''
# n= str(input("Enter a string : "))
# s=n.split(" ")
# for i in s:
#     if len(i)%2==0:
#         print(i)




'''Python Program to Count the Number of matching characters in a pair of string'''
# using intersection taking common
# def commonfun(str1,str2):
#     return(len((set(str1)).intersection(set(str2))))
#
# string1=str(input("Enter first string : "))
# string2=str(input("Enter second string : "))
#
# no_of_common_character=commonfun(string1.lower(),string2.lower())
#
# print("NUMBER OF COMMON CHRACTERS ARE : ",no_of_common_character)