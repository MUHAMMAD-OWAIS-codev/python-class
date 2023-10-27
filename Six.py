# print("owais")
# file handing
# open()   #file open or read file data
# f=open("file.txt","r")
# content=f.readline()
# print(content)
# read a file using readlines method
# f=open("file.txt","r")
# content=f.readline()
# print(len(content))
# print(content)
# read a file using readline method
# f=open("file.txt","r")
# row=f.readline()
# print(row)
# row=f.readline()
# print(row)
# # replace
# f= open("text.txt","a")
# f.write("\n1 more hello world")
# f.close()
# f = open("text.txt","r")
# content = f.read()
# print(content)
# f=open("new_file_1.txt","w")

# print("pointer position:",f.tell()) #pointer position 0

# f.read("123")

# print("pointer position:") # position posi 

# f.seek(0) #set pointer  position to 0

# print("pointer position",f.tell()) # pointer position 4
 
# f.write("abcd 123123") 
 
# f= open ("new_file_1.txt","a+")

# print("pointer position:",f.tell())

# content=f.read()
# print("content",content)

# f.write("using append method line 1\n")
# f.write("using append method line 2\n")
# print(content)
# import time
# f=open("new_file_1.txt","w")
# for i in range(60):
#     print("line",i)
#     f.write("line" + str(i) + "\n")
#     time.sleep(1)
#     f.flush()
# f.close()
# import time
# f=open("new_file_1.txt","w")
# for i in range(60):
#     print("line",i)
#     f.write("line" + str(i) + "\n")
#     if i %10==0:
#         print("flushed")
#     f.flush()
#     time.sleep(1)
# f.close()
# import os
# current_working_dir=os.getcwd()
# print(current_working_dir)
# print(__file__)
# print(current_working_dir)
# print(os.listdir())
# files_and_folders_in_dir=os.listdir()
# print(path)
# import os
# current_working_dir=os.getcwd()
# print(current_working_dir)
# path=os.path.join("..", "parent_file.txt")
# os.path.abspath("parent")
# print(__file__)
