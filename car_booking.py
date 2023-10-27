import pytz
from datetime import datetime

# Define a list to store bookings
store_booking = []

# Function to check if a time slot is available
def is_slot_available(start_date, end_date, car_model):
    for booking in store_booking:
        if (
            booking["start_date"] <= start_date <= booking["end_date"]
            or booking["start_date"] <= end_date <= booking["end_date"]
            or start_date <= booking["start_date"] <= end_date
        ):
            car_models = booking["car_model"].split(", ")
            if car_model in car_models:
                return False
    return True

print("Welcome to ABC Hotel Booking System")

# Loop to get user input and make bookings
for i in range(5):  # You mentioned the loop should run 5 times
    start_date_str = input("Enter Start Date and Time (YYYY-MM-DD HH:MM:SS): ")
    end_date_str = input("Enter End Date and Time (YYYY-MM-DD HH:MM:SS): ")
    timezone_str = input("Enter Timezone (e.g., Asia/Karachi): ")
    car_model = input("Enter Car Model (e.g., Corolla): ")

    # Convert user input to datetime objects
    start_date = datetime.fromisoformat(start_date_str)
    end_date = datetime.fromisoformat(end_date_str)

    # Convert the user's specified timezone to a timezone object
    user_timezone = pytz.timezone(timezone_str)

    # Make the start and end dates timezone-aware
    start_date_tz_aware = user_timezone.localize(start_date)
    end_date_tz_aware = user_timezone.localize(end_date)

    # Convert to UTC timezone for storing
    utc_timezone = pytz.timezone("UTC")
    utc_start_date = start_date_tz_aware.astimezone(utc_timezone)
    utc_end_date = end_date_tz_aware.astimezone(utc_timezone)

    # Check if the slot is available
    if is_slot_available(utc_start_date, utc_end_date, car_model):
        # If available, store the booking
        store_booking.append({
            "start_date": utc_start_date,
            "end_date": utc_end_date,
            "car_model": car_model
        })
        print("Booking Successful")
    else:
        print("Slot Already Booked")

# You can print the final list of bookings if needed
# print(store_booking)