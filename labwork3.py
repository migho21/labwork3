'''
 Program purpose: To develop Mighobae Hotel Reservation System
 Developer: Muhammad Amirul Aiman Bin Muhamad Azani
 Date: 1 March 2024
'''

from datetime import datetime

print("\nWelcome to our Mighobae Hotel Reservation System\n")
room_types = ["Single Room", "Double Room", "Suite"]
nightly_rates = [100, 150, 250]
additional_services = {"Breakfast": 20, "WiFi": 10, "Parking": 15}

for i, room in enumerate(room_types):
    print(f"{i + 1}. {room} - RM{nightly_rates[i]} per night")

room_choice = int(input("\nPlease select a room type (1/2/3): "))
number_of_rooms = int(input("\nEnter the number of rooms: "))
check_in = input("\nEnter your check-in date (YYYY-MM-DD): ")
check_out = input("Enter your check-out date (YYYY-MM-DD): ")

days_stayed = (datetime.strptime(check_out, "%Y-%m-%d") - datetime.strptime(check_in, "%Y-%m-%d")).days
room_cost = nightly_rates[room_choice - 1] * number_of_rooms * days_stayed

print("\nAdditional Services:")
for i, (service, cost) in enumerate(additional_services.items()):
    print(f"{i + 1}. {service} - RM{cost} per person/day")

additional = input("\nWould you like to add any additional services? (yes/no): ").lower()

selected_services = {}
additional_cost = 0
if additional == 'yes':
    services_input = input("Please select additional services (separated by commas, e.g., 1,2): ")
    services_list = [int(x.strip()) for x in services_input.split(',')]

    for service in services_list:
        if service == 1:
            additional_cost += additional_services["Breakfast"] * number_of_rooms * days_stayed
            selected_services["Breakfast (2 persons)"] = additional_services[
                                                             "Breakfast"] * number_of_rooms * days_stayed
        elif service == 2:
            additional_cost += additional_services["WiFi"] * days_stayed
            selected_services["WiFi (2 days)"] = additional_services["WiFi"] * days_stayed
        elif service == 3:
            additional_cost += additional_services["Parking"] * days_stayed
            selected_services["Parking (2 days)"] = additional_services["Parking"] * days_stayed

total_cost = room_cost + additional_cost

# Adjust the breakfast cost output
if "Breakfast (2 persons)" in selected_services:
    selected_services["Breakfast (2 persons)"] = additional_services["Breakfast"] * 2 * days_stayed

print("\nThank you for your reservation.")
print("\nReservation Details:")
print(f"Room Type: {room_types[room_choice - 1]}")
print(f"Number of Rooms: {number_of_rooms}")
print(f"Check-in Date: {check_in}")
print(f"Check-out Date: {check_out}")
print("\nAdditional Services:")
for service, cost in selected_services.items():
    print(f"- {service} - RM{cost}")
print(f"\nTotal Cost: RM{total_cost}")

confirm = input("\nWould you like to confirm your reservation? (yes/no): ").lower()
if confirm == 'yes':
    print("Reservation confirmed. Thank you for choosing our hotel. Enjoy your stay!")
else:
    print("Reservation cancelled. Feel free to book again anytime.")
