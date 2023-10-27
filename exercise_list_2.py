# 1. Write a Python program to multiply all the items in a list and use for loop. consider the list [3, 5, 2, 1, 4].
# output should be 360
# list_items = [3, 5, 2, 1, 4]
# x = list_items[0]
# for item in list_items:
#   x *= item
# print(x)
# 2. create a list from 0 to 100 using range function and iterate over the list
# display the number that satisfied following conditions
# The number must be divisible by 5
# If the number is greater than 30 and less than 50 then skip it
# If the number is greater than 80, then stop the loop
# for i in range(0, 101):
#   if i % 5 == 0:
#     if i > 30 and i < 50:
#       continue
#     elif i > 80:
#       break
#     else:
#       print(i)
# 3. consider the following list ['cat', 'dog', 'hand', 'freedom', 'jump', 'frog', 'happy', 'popcorn', 'tiger']
# display the word that contains character longer than 5
# the output should be freedeom and popcorn
# word_list = ['cat', 'dog', 'hand', 'jump', 'frog', 'happy', 'popcorn', 'tiger']
# for word in word_list:
#     if len(word) > 5:
#         print("is declare on list",word)
# 4. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements using for loop. Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'] Expected Output : ['Green', 'White', 'Black']
# list_elements = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# print("Original list:", list_elements)
# new_list = []
# for i in range(len(list_elements)):
#         if i != 0 and i != 3 and i != 4:
#               new_list.append(list_elements[i])
# print("Modified list:", new_list)
# 5. Write a program to display odd numbers only. odd number upto 100
# hint use for loop and range function                                                                                                                            without  def 
# a = int(input("Enter the start of range:"))
# b = int(input("Enter the end of range:")) 
# for num in range(a, b + 1):
#     if num % 2 != 0:
#         print(num)
# 6. List contains 30 elements. Display first 5 and last 5 elements
# list_elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
#                  11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
#                  21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
# first_5_elements = list_elements[:5]
# last_5_elements = list_elements[-5:]
# print("First 5 elements:", first_5_elements)
# print("Last 5 elements:", last_5_elements)
# 7. Display output: helloworld from the list [‘h’, ‘e’, ‘l’, ‘l’, ‘o’, ‘w’, ‘o’, ‘r’, ‘l’, ‘d’]
# output should be 'helloworld' in one line
# letters = ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']
# print(''.join(letters))
# 8. Write a Python program to append a list to the second list.
# consider l1 is [1, 2, 3, 4, 5] and l2 is []
# using loop add items of l1 in l2
# l1 = [1, 2, 3, 4, 5]
# l2 = []
# for i in l1:
#     l2.append(i)
# print(l2)
# 9. consider the list ['hi', 'hello', 'hi', 'good morning', 'hi', 'bye']
# use for loop and find the count that how many times the word "hi" present in list.
# output should be 3
# list_of_words = ['hi', 'hello', 'hi', 'good morning', 'hi', 'bye']
# count = 0
# for word in list_of_words:
#     if word == 'hi':
#         count += 1

# print(count)
