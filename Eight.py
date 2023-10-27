# import pytz

# booking_storage = []

# def is_time_slot_available(start_date, end_date):
#     utc = pytz.utc
#     for booking in booking_storage:
#         booked_start = booking["start_date"]
#         booked_end = booking["end_date"]
        
#         # Check if the provided time slot overlaps with any existing bookings
#         if start_date < booked_end and end_date > booked_start:
#             return False
#     return True

# # Loop to accept user input and check availability
# for m in range(5):
#     start_date_str = input(f"Enter start date and time for booking {m+1} (YYYY-MM-DD HH:MM:SS): ")
#     end_date_str = input(f"Enter end date and time for booking {m+1} (YYYY-MM-DD HH:MM:SS): ")
#     timezone_str = input(f"Enter timezone for booking {m+1} (e.g., US/Pacific): ")
    
#     start_date = pytz.timezone(timezone_str).localize(pytz.datetime.datetime.strptime(start_date_str, "%Y-%m-%d %H:%M:%S"))
#     end_date = pytz.timezone(timezone_str).localize(pytz.datetime.datetime.strptime(end_date_str, "%Y-%m-%d %H:%M:%S"))
#     utc_aware_date = start_date.astimezone(pytz.utc)
#     utc_aware_end_date = end_date.astimezone(pytz.utc)
#     if is_time_slot_available(utc_aware_date, utc_aware_end_date):
#         print("Malik Booking is succesfully Done!")
#         # break
#     else:
#         print("Malik Seat nhi hai")

# # Display the booked time slots
# print("\nBooked Time Slots:")
# for booking in booking_storage:
#     print(f"Start Date: {booking['start_date']} | End Date: {booking['end_date']}")

##########################################################################################
#slice
# x = "Hello World"
# characters = x[4:10]
# print(characters)

# list_one = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_one[0:5])
# print(list_one[5:10])
# list_two = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list_two[2:5])
# print(list_two[7:])
# print(list_two[1:8:2])

#Split function
#String Function
# Converting string into list
# sentence = "This is a simple sentence"
# csv_data  = "Alice, Bob, Charlie, David"
# date_str = "2023-12-21"
# Multiline_txt = """
# Line 1
# Line 2
# Line 3
# """
# url = "https://google.com/path/method"

# print(sentence.split(" "))
# print(csv_data.split(","))
# print(date_str.split("-"))
# print(Multiline_txt.split("\n"))
# print(url.split("/"))

# Converting list into string
# words = ["This", "is", "a", "simple", "sentence"]
# sentens = " ".join(words)
# print(sentens)

# names = ["Alice", "Bob", "Charlie"]
# date_parts = ["2023","09", "01"]
# numbers = [100, 102, 103, 104]
# numbers_str = (list(map(str, numbers)))
# sen = ",".join(names)
# print(sen)
# sens = "-".join(date_parts)
# print(sens)
# sentenc = " ".join(numbers_str)
# print(sentenc)

#sequence Datatypes
#String
#list (ordered Datatype)    [1, 2, 3 ,4 ,5] (Mutable (means ke meory location nahi change hogi koi bhi operation perform karne ke liye))
#Tuple (ordered Datatype)   (1, 2, 3, 4, 5) (IMMutable)
#sets (Un-ordered Datatype)  {1, 2, 3, 4, 5 , 2} Ye duplicate values nahi print karega (mutable data type (means ke agar koi bhi data add karunga to memory location change hojayegi or memory location pata karne ke liy id ka methid use karte hain (id(ismein jiski memory location chekc karni ho use likhte hain))))
#Set Methods
# s.discard()
# s.remove()
# s.update()
# s.union()
# s.intersection()
# s.difference()


# set_A = {1, 2, 3, 4, 5}
# set_B = {4, 5, 6, 7, 8}

# print(set_A.union(set_B))
# print(set_A.intersection(set_B))
# print(set_A.difference(set_B))
# print(set_A.add(10))
# print(set_B.add(10))
# print(set_B.add(10))

# number  = 3
# if number in set_A and number in set_B:
#     print("Han bhai available hai")
# else:
#     print("Not Available")