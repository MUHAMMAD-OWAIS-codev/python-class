from datetime import date, timedelta

class Hotel:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def total_rooms(self):
        return len(self.rooms)

    def display_info(self):
        print(f"Hotel Name: {self.name}, Address: {self.address}")


class Room:
    def __init__(self, name, num_of_beds, fare_per_day):
        self.name = name
        self.num_of_beds = num_of_beds
        self.fare_per_day = fare_per_day
        self.bookings = []

    def check_availability(self, start_date):
        for booking in self.bookings:
            if start_date >= booking['start_date'] and start_date <= booking['end_date']:
                return False
        return True

    def book(self, start_date, end_date):
        if self.check_availability(start_date):
            self.bookings.append({'start_date': start_date, 'end_date': end_date})
            return True
        return False


class BookingSystem:
    def __init__(self):
        self.hotels = []

    def create_hotel(self, name, address):
        hotel = Hotel(name, address)
        self.hotels.append(hotel)
        return hotel

    def get_hotel(self, name):
        for hotel in self.hotels:
            if hotel.name == name:
                return hotel
        return None


# Create a booking system
booking_system = BookingSystem()

# Create a hotel
hotel_name = input("Enter hotel name: ")
hotel_address = input("Enter hotel address: ")
hotel = booking_system.create_hotel(hotel_name, hotel_address)

# Create rooms for the hotel
while True:
    room_name = input("Enter room name (or 'done' to finish adding rooms): ")
    if room_name.lower() == 'done':
        break
    num_of_beds = int(input("Enter number of beds: "))
    fare_per_day = float(input("Enter fare per day: "))
    room = Room(room_name, num_of_beds, fare_per_day)
    hotel.add_room(room)

# Check room availability and book
start_date = input("Enter booking start date (YYYY-MM-DD): ")
end_date = input("Enter booking end date (YYYY-MM-DD): ")

start_date = date.fromisoformat(start_date)
end_date = date.fromisoformat(end_date)

for room in hotel.rooms:
    if room.check_availability(start_date):
        if room.book(start_date, end_date):
            print(f"Room '{room.name}' is booked from {start_date} to {end_date}")
        else:
            print(f"Room '{room.name}' is already booked for the selected dates")

# Display hotel info
hotel.display_info()

# Get total rooms in the hotel
print(f"Total rooms in '{hotel.name}' are {hotel.total_rooms()}")
