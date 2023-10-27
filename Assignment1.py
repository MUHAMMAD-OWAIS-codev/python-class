# Assignment "If Statement"
# Write a program to check whether a person is eligible to vote or not?
# exercise_1
# age = int(input("Enter age : "))
# if age >= 18:
#     print("Eligible for Voting!")
# else:
#     print("Not Eligible for Voting!")
# Write a program to check char is vowel or not.
# exercise_2
# x=input("Enter your vowel")
# if x=="a":
#     print(x,"its a vowel")
# elif x=="e":
#     print(x,"its e vowel")
# elif x=="i":
#     print(x,"its i vowel")
# elif x=="o":
#     print(x,"its o vowel")
# elif x=="u":
#     print(x,"its u vowel")
# else:
#     print(x,"its not a vowel ")
# Write a program to check the number is positive or negative. User input.
# exercise_3
# n = float(input("Input a number: "))
# if n >= 0:
#   if n == 0:
#       print("It is Zero!")
#   else:
#       print("Number is Positive number.")
# else:
#   print("Number is Negative number.")
# Write a program to check whether a number is odd or even?
# exercise_4
# num = int(input("Enter a Number:"))
# if num % 2 == 0:
#   print(num , "is even")
# else:
#   print(num , "is odd")
# Write a program to display the grade of the user in subject A, ask user marks obtained out of 100
# exercise_5
# x=input("enter your value")
# z=int(x)
# if z<=100 and z>=80:
#     print("its a 'A'Grade ")
# elif z<=70 and z>=60:
#     print("its a 'B'Grade ")
# elif z<=50 and z>=40:
#     print("its a 'c'Grade ")
# else:
#     print("ap fail ho bhai")
# Write a program to check whether a number is divisible by 7
# exercise_6
# x = int(input("Enter a number:"))
# if(x%7==0):
#      print(x,"is divisible by 7")
# else:
#      print(x,"is NOT divisible by 7.")
# Write a program to check if year is leap year.
# exercise_7
# year = int(input("Enter a year: "))
# if year % 400 == 0 or (year % 4 == 0 and year % 100== 0):
#     print(year, "is a leap year")
# else:
#     print(year, "is not a leap year")
# Write a program to ask user its name and check whether name consists of 5 or more letters
 # exercise_8
# name = input("Enter your name: ")
# if len(name) >= 5:
#   print(f"Your name {name} has 5 or more letters.")
# else:
#   print(f"Your name {name} does not have 5 or more letters.")
# Write a program that accepts 3 inputs from user. input 1 and input 2 should be numbers and the third input should be mathematical operator. Perform operation accordingly
# exercise_9
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# x = input("Enter the mathematical  operator (+, -, *, /): ")
# if x == '+':
#     result = num1 + num2
# elif x == '-':
#     result = num1 - num2
# elif x == '*':
#     result = num1 * num2
# elif x == '/':
#     result = num1 / num2
# else:
#     print("Invalid x.")
# print("The result is:", result)
# Write a program that accepts 1 input from user and check if the number is divisible by 2 and 3 both.
# # exercise_10
# number = int(input("Enter a number: "))
# if number % 2 == 0 and number % 3 == 0:
#   print(f"{number} is divisible by 2 and 3")
# elif number % 2 == 0:
#   print(f"{number} is only divisible by 2")
# elif number % 3 == 0:
#   print(f"{number} is only divisible by 3")
# else:
#   print(f"{number} is not divisible by 2 or 3")
# Write a program that accepts 2 inputs from user and check which number is largest.
# # exercise_11
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# if number1 > number2:
#   print(f"The larger number is {number1}")
# else:
#   print(f"The larger number is {number2}")
# Write a program that accepts 3 input from user and check which number is largest.
 # exercise_12
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# number3 = int(input("Enter the third number: "))
# largest_number = number1
# if number2 > largest_number:
#   largest_number = number2
# if number3 > largest_number:
#   largest_number = number3
# print(f"The largest number is {largest_number}")
# Write a program that accepts 3 input from user and check the second is largest.
 # exercise_12
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# number3 = int(input("Enter the third number: "))
# if number2 > number1 and number2 < number3:
#   print(f"The second number is the largest number {number2}")
# else:
#   print(f"The second number is not the largest number")
# Write a program that accepts 3 input from user and check the second is largest.
# exercise_13
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# number3 = int(input("Enter the third number: "))

# if number2 > number1 and number2 < number3:
#     print(f"The second number is the largest number {number2}")
# else:
#     if number2 == number1:
#         print(f"The second number is equal to the first number {number2}")
#     elif number2 == number3:
#         print(f"The second number is equal to the third number {number2}")
#     else:
#         print(f"The second number is not the largest number")
# Write a python program that accept user an input. The valid input should be of following
# exercise_14
# traffic_light = input("Enter a traffic light: ")
# if traffic_light == "green":
#   print("Car is allowed to go")
# elif traffic_light == "red":
#   print("Car has to stop")
# elif traffic_light == "yellow":
#   print("Car has to wait")
# else:
#   print("Invalid input")
# Write a program to trace your subject mark. Your program should fulfill the following conditions:
# exercise_15
# a = int(input("Enter your subject  mark: "))

# if a < 0 or a > 100:
#   print("Error: a should be between 0 and 100 only")
# elif a < 50:
#   print("You are fail")
# else:
#   if a <= 60:
#     print("You are pass. Remark: Good")
#   elif a <= 80:
#     print("You are pass. Remark: Very Good")
#   else:
#     print("You are pass. Remark: Outstanding")
###########################list_array#############
# Create a list of juices, add 5 items using append
# exercise_1
# juices = []
# juices.append("Orange")
# juices.append("Apple")
# juices.append("Mango")
# juices.append("Pineapple")
# juices.append("Watermelon")
# print(juices)
# Create a list of cars, add 5 items using insert
# exercise_2
# cars = []
# cars.insert(0, "Tesla")
# cars.insert(1, "BMW")
# cars.insert(2, "Mercedes")
# cars.insert(3, "Audi")
# cars.insert(4, "Porsche")
# print(cars)
# Remove last item from the list [‘bed’, ‘table’, ‘chair’, ‘sofa’]	using pop and len 
# exercise_3
# items = ['bed', 'table', 'chair', 'sofa']
# last_item = items.pop()
# print(items)
# Remove second last item from the list [‘bed’, ‘table’, ‘chair’, ‘sofa’] by len and index
# exercise_4
# items = ['bed', 'table', 'chair', 'sofa']
# length = len(items)
# second_last = length - 2
# items.pop(second_last)
# print(items)
# Remove first item from the list [‘bed’, ‘table’, ‘chair’, ‘sofa’]
# exercise_5
# items = ['bed', 'table', 'chair', 'sofa']
# last_item = items.pop(0)
# print(items)
# Remove the item “chair” from the list [‘bed’, ‘table’, ‘chair’, ‘sofa’]
# exercise_6
# items = ['bed', 'table', 'chair', 'sofa']
# last_item = items.pop(2)
# print(items)
# Remove all “chair” from the list [‘bed’, ‘table’, ‘chair’, ‘sofa’, ‘chair’]
# exercise_7
# list_items=['bed','table','chair','sofa','chair']
# for item in list_items:
#     if item=='chair':
#         list_items.remove(item)
# print(list_items)
# Merge two lists [‘A’, “B”, “C”] and [“D”, “E”, “F”]
#  exercise_8
# list1 = ["A", "B", "C"]
# list2 = ["D", "E", "F"]
# merged_list = list1 + list2
# print(merged_list)
# Write a Python program to check if a list is empty or not.
#  exercise_9
# list1 = ['']
# if not list1:
#   print("The list is empty.")
# else:
#   print("The list is not empty.")
########Assignment1######