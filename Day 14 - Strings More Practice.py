'''Count Vowels and Consonants'''
# def count_vowels_consonants(s):
#     vowels = "aeiouAEIOU"
#     v_count = sum(1 for char in s if char in vowels)
#     c_count = sum(1 for char in s if char.isalpha() and char not in vowels)
#     return v_count, c_count
#
# n = input("Enter : ")
# vowels, consonants = count_vowels_consonants(n)
# print(f"Vowels: {vowels}, Consonants: {consonants}")




'''Count occurrences of each Character'''
# from collections import Counter
#
# def character_frequencies(s):
#     return Counter(s)
#
# n = input("Enter : ")
# print(character_frequencies(n))



'''First non-repeating Character'''
# def first_non_repeating_char(s):
#     frequency = {}
#     for char in s:
#         frequency[char] = frequency.get(char, 0) + 1
#     for char in s:
#         if frequency[char] == 1:
#             return char
#     return None
#
# n = input("Enter : ")
# print(first_non_repeating_char(n))




'''Check For Substring'''
# def is_substring(s1, s2):
#     return s2 in s1
#
# s1 = input("Enter 1st String : ")
# s2 = input("Enter 2nd String : "  )
# print(is_substring(s1, s2))
# print(is_substring(s1, s2))
