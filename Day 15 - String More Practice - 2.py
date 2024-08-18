'''Python Program to remove all duplicates from a given string'''
# string = str(input("Enter a string : "))
# p = ""
# for char in string:
#     if char not in p:
#         p = p+char
# print(p)
# k = list(string)




'''Python – Least Frequent Character in String'''
# initializing string
# test_str = str(input("Enter a String : "))
#
# # printing original string
# print ("The original string is : " + test_str)
#
# # using naive method to get
# # Least Frequent Character in String
# all_freq = {}
# for i in test_str:
#     if i in all_freq:
#         all_freq[i] += 1
#     else:
#         all_freq[i] = 1
# res = min(all_freq, key = all_freq.get)
#
# # printing result
# print("The Minimum of all characters in {test_str} is : " + str(res))




'''Python | Maximum frequency character in String'''
# initializing string
# test_str = str(input("Enter a String : "))
#
# # printing original string
# print ("The original string is : " + test_str)
#
# # using naive method to get
# # Maximum frequency character in String
# all_freq = {}
# for i in test_str:
#     if i in all_freq:
#         all_freq[i] += 1
#     else:
#         all_freq[i] = 1
# res = max(all_freq, key = all_freq.get)
#
# # printing result
# print(f"The Maximum of all characters in {test_str} is : " + str(res))




'''Python - Program to check if a string contains any special character'''
def contains_special_characters(input_string):
    # Define a set of special characters
    special_characters = set('!@#$%^&*(),.?":{}|<>')

    # Iterate over each character in the string
    for char in input_string:
        if char in special_characters:
            return True
    return False

# Example usage:
input_string = str(input("Enter a String : "))
if contains_special_characters(input_string):
    print("The string contains special characters.")
else:
    print("The string does not contain any special characters.")