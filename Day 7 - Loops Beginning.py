#7th Day - Thala For A Reason.
#Starting LOOPS in PYTHON


'''To Print 10 Natural Numbers Using Whiile Loop'''
# i = 1
# while i <= 10:
#     print(i)
#     i += 1
#     # i += 1 is used to increment the value of i by 1 in each iteration of the while loop.
#     # "+=" is an addition and assignment operator.




'''Use Loop to Iterate lists, tuples, strings and dictionaries in Python.'''
# print("List Iteration")
# l = ["Thala", "For", "A", "Reason"]
# for i in l:
#     print(i)
#
#
# print("\nTuple Iteration")
# t = ("Thala", "For", "A", "Reason")
# for i in t:
#     print(i)
#
#
# print("\nString Iteration")
# s = "THALA"
# for i in s:
#     print(i)
#
#
# print("\nDictionary Iteration")
# d = dict()
# d['xyz'] = 123
# d['abc'] = 345
# for i in d:
#     print("%s  %d" % (i, d[i])) #In this code, d is a dictionary with two key-value pairs: 'xyz' with value 123 and 'abc' with value 345. The for loop iterates over the keys of the dictionary d. Inside the loop, the key i is used to access the corresponding value using d[i]. The %s and %d are placeholders for string and integer formatting, respectively.
#
#
# print("\nSet Iteration")
# set1 = {2, 0, 0, 7}
# for i in set1:
#     print(i),




'''Calculate the sum of all numbers from 1 to a given number'''
# sum = 0
# n = int(input("Enter Number till Sum you want : "))
# for i in range(1, n+1, 1):
#     sum += i
#     print("The sum is : ", sum)




'''Write a program to print Multiplication table of a given number'''
# num = int(input("Enter Number whose Table you want : "))
# for i in range(1,11):
#     print(f"{num} * {i} = {num*i}")