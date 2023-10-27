# Pass by value 
# name_first = "Muhammad"
# def name(name_first):
#     name_first = "Owais"
#     print(name_first)
# print(name(name_first))

# # Pass by reference
# list = ["Muhammad"]
# def name_first(list):
#     Changes = list.append("Owais")
#     print(Changes)
# print(name_first(list))
# print(list)

# list = [1, 2, 3, 4]
# def add_item(elem):
#     list.append(elem)

# add_item(5)
# print(list)

# x = 10
# def change_val():
#     global x
#     x  = 100000000000000000000000


# change_val()
# print(x)

# counter = 0
# def increment():
#     global counter
#     counter += 1

# def decrement():
#     global counter
#     counter -= 1

# for i in range(5):
#     increment()
# print(counter)
# for i in range(2):
#     decrement()
# print(counter)

# Pass by value 
# name_first = "Muhammad"
# def name(name_first):
#     name_first = "Owais"
#     print(name_first)
# print(name(name_first))

# # Pass by reference
# list = ["Muhammad"]
# def name_first(list):
#     Changes = list.append("Owais ")
#     print(Changes)
# print(name_first(list))
# print(list)

# list = [1, 2, 3, 4]
# def add_item(elem):
#     list.append(elem)

# add_item(5)
# print(list)

# x = 10
# def change_val():
#     global x
#     x  = 100000000000000000000000


# change_val()
# print(x)

# counter = 0
# def increment():
#     global counter
#     counter += 1

# def decrement():
#     global counter
#     counter -= 1

# for i in range(5):
#     increment()
# print(counter)
# for i in range(2):
#     decrement()
# print(counter)
# class Employee():
#     counter = 0 #! This is class level information and this information should get shared agar ye ap class ke kitne hi instances kyun na banao ye wahan accessible hogi or agar isko class ke through change karenge to ye saare objects ke liye change hoga or agar specific object ke through access ya change karne ki koshish karenge to sirf us specific object ke liye change hoga
#     def __init__(self, first_name, last_name, salary):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.salary = salary
#         Employee.counter += 1
#     def get_fullname(self):
#         full_name = self.first_name + " " + self.last_name
#         return full_name
#     def get_email(self): #? Instance methods / Methods but they are not called as functions and self argument should be passed otherwise it will give error
#         email = self.first_name + self.last_name + "@gmail.com"
#         return email

# #TODO Instance properties are passed when making the instance(object) of the class
# obj_one = Employee("Mustafa", "Kashif", 1500000000) #! This is the instance of the class (Also known as object)
# print(obj_one.first_name)
# print(obj_one.__dict__)
# print(obj_one.get_fullname())
# print(obj_one.get_email())
# obj_one.counter = 10000
# obj_two = Employee("Kashif", "Mehmood", 1500000000) #! This is the instance of the class (Also known as object)
# print(obj_two.first_name)
# print(obj_two.__dict__)
# print(obj_two.get_fullname())
# print(obj_two.get_email())
# # Employee.counter = 100
# print(obj_two.counter) #! Agar obj level par class level information ko manipulate nahi kiya jaye to wo class level information ko hi use karega otherwise obj level manipulated use karega sirf wohi object jise call karke wo info manipulate ki gayi ho
# print(obj_one.counter)
