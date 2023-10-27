# Write a Python program to copy a list using for loop. consider a list
# li = [1, 2, 3, 4]
# li_2 = []
# use for loop and add al the items in li_2
# li = [1, 2, 3, 4]
# li_2 = []
# for i in li:
#   li_2.append(i)
# print(li_2)
# Write a Python function that takes two lists and returns True if they have at least one common member.
# consider list l1 = [1, 2, 3, 4] and l2 = [5, 6, 7, 3]
# in both list value "3" is common
# use for loop
# hint: nested loop 
# l1 = [1, 2, 3, 4]
# l2 = [5, 6, 7, 3]
# common_found = False
# for item1 in l1:
#     for item2 in l2:
#         if item1 == item2:
#             common_found = True
#             break  
#     if common_found:
#         break  
# if common_found:
#     print(" The lists have at least one common member.")
# else:
#     print("The lists do not have any common members.")
# Write a program to display index and the values (both) of a list using for loop. consider a list l = [100, 200, 300, 400]
# output: 
# 0 100
# 1 200
# 2 300
#  3 400
# l = [100, 200, 300, 400]
# for i, value in enumerate(l):
#     print(i, value)
# Write a program that find common values between 2 lists and also tells how many times the common value occurs.
# consider the list l1 = ['a', 'b', 'c', 'd'] and l2 = ['e', 'b', 'g', 'd', 'f', 'h']
# l1 = ['a', 'b', 'c', 'd']
# l2 = ['e', 'b', 'g', 'd', 'f', 'h']
# results = {}
# for value in l1:
#     if value in l2:
#         if value not in results:
#             results[value] = 1
#         else:
#             results[value] += 1
# print(results)
# consider the number 2783, the number consists of 4 digits.
# Count the total number of digits in a number using while loop.
# instruction (hint):
# x = 2783
# counter = 0
# run while loop as long as x becomes 0
# increment the counter inside while loop
# divide x by 10 using floor division syntax "//"
# x = 2783
# counter = 0
# while x > 0:
#     x //= 10
#     counter += 1
# print(counter)
# Write a program that takes user input and display it. The program keep ask user the input until user enters “0”
# user_input = ("Enter number")
# while user_input != "0":
#     user_input = input("Enter a number: ")
#     print("You entered:", user_input)
# Write a program and ask user to enter number, 5 times using while loop. store each value in list.
# calculate the sum of all values in a list
# numbers = []
# i = 0
# while i < 5:
#     number = int(input("Enter a number: "))
#     numbers.append(number)
#     i += 1
# sum_of_numbers = 0
# for number in numbers:
#     sum_of_numbers += number
# print("The sum of the numbers is:", sum_of_numbers)
# Write a program to keep asking for a number until you enter a negative number. At the end, print the sum of all entered numbers.
# num = 0
# sum = 0
# while num >= 0:
#     num = int(input("Enter a number (or negative number to quit): "))
#     if num >= 0:
#         sum += num
# print("The sum of all entered numbers is:", sum)
# Write a program to ask for a name until the user enters END. Print the name each time. When you are done, print "I am done."
# consider the list l1 [11, 33, 50]. use for loop to output the result like "113350"
# l1 = [11, 33, 50]
# name = ""
# while name!= "END":
#     name = input("Enter a name (or END to quit): ")
#     if name!= "END":
#         print(name)
# print("I am done.")
# Write a Python program to copy a dict using for loop. consider a dict
# d1 = {"id": 1, "name": "your-name", "gender": "male"}
# d2 = {}
# use for loop and add al the items in d2
# d1 = {"id": 1, "name": "your-name", "gender": "male"}
# d2 = {}
# for key, value in d1.items():
#     d2[key] = value
# print(d2)