#A substring is a contiguous sequence of characters within a larger string. It is a part of the original string. ex- substrings of "Iam Techunt" are: Iam, Iam Te, Iam T, Iam Tech, I, am, a, m, T,,,,............................etc.
'''Python | Check if a Substring is Present in a Given String'''
# string = str(input("Enter a String : "))
# substring = str(input("Enter a Substring : "))
# s = string.split()
# if substring in s:
#     print("yes")
# else:
#     print("no")




'''Python – All substrings Frequency in String'''
# def substring_frequencies(s):
#     freq_dict = {}
#
#     # Generate all possible substrings
#     for i in range(len(s)):
#         for j in range(i + 1, len(s) + 1):
#             substring = s[i:j]
#             if substring in freq_dict:
#                 freq_dict[substring] += 1
#             else:
#                 freq_dict[substring] = 1
#
#     return freq_dict
#
# # Example usage:
# input_string = str(input("Enter a String : "))
# result = substring_frequencies(input_string)
# print(result)




'''Python – Maximum occurring Substring from list'''
# # initializing string
# test_str = "subscibetocodevtomakemeviralsubscribemysubscribeiamcodevsubscribemycodevtomakemeviralsubscribesubscribetomysponsorshipp."
# test_list = ['subscribe', 'to', 'codev']
#
# # printing original string and list
# print("The original string is : " + test_str)
# print("The original list is : " + str(test_list))
# res = []
# for i in test_list:
#     res.append(test_str.count(i))
# x = max(res)
# result = test_list[res.index(x)]
# # printing result
# print("Maximum frequency substring : " + str(result))




'''Python – Possible Substring count from String'''
test_str = "tcheontutecheaecht"

# printing original string
print("The original string is : " + str(test_str))

# initializing arg string
arg_str = "tech"

# using min and count to get minimum possible
# occurrence of character
res = min(test_str.count(char) // arg_str.count(char) for char in set(arg_str))

# printing result
print("Possible substrings count : " + str(res))