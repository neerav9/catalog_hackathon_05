# EV Charging Station Finder and Slot Booking Console Application
charging_stations = [
    {"name": "Station A", "location": "Downtown", "connector_type": "Type 2", "available_slots": 5},
    {"name": "Station B", "location": "Suburb", "connector_type": "Type 1", "available_slots": 2},
    {"name": "Station C", "location": "City Center", "connector_type": "CHAdeMO", "available_slots": 3},
    {"name": "Station D", "location": "Airport", "connector_type": "Type 2", "available_slots": 1},
    {"name": "Station E", "location": "Mall", "connector_type": "CCS", "available_slots": 4},
]

def display_stations(stations):
    print(f"{'Station Name':<15}{'Location':<15}{'Connector Type':<15}{'Available Slots':<15}")
    print("-" * 60)
    for station in stations:
        print(f"{station['name']:<15}{station['location']:<15}{station['connector_type']:<15}{station['available_slots']:<15}")
    print("\n")

def find_stations(location=None, connector_type=None):
    filtered_stations = []
    for station in charging_stations:
        if (location is None or station["location"].lower() == location.lower()) and \
           (connector_type is None or station["connector_type"].lower() == connector_type.lower()):
            filtered_stations.append(station)
    return filtered_stations

def book_slot(station_name):
    for station in charging_stations:
        if station["name"].lower() == station_name.lower():
            if station["available_slots"] > 0:
                station["available_slots"] -= 1
                print(f"Slot successfully booked at {station['name']}!\n")
            else:
                print(f"Sorry, no available slots at {station['name']}.\n")
            return
    print(f"Charging station '{station_name}' not found.\n")

def main():
    print("Welcome to the EV Charging Station Finder and Slot Booking System!\n")
    while True:
        print("1. View All Charging Stations")
        print("2. Find Charging Station by Location")
        print("3. Find Charging Station by Connector Type")
        print("4. Book a Charging Slot")
        print("5. Exit")
        choice = input("Please choose an option (1-5): ")

        if choice == '1':
            display_stations(charging_stations)

        elif choice == '2':
            location = input("Enter the location to search: ")
            filtered_stations = find_stations(location=location)
            if filtered_stations:
                display_stations(filtered_stations)
            else:
                print("No stations found for the given location.\n")

        elif choice == '3':
            connector_type = input("Enter the connector type (Type 1, Type 2, CHAdeMO, CCS): ")
            filtered_stations = find_stations(connector_type=connector_type)
            if filtered_stations:
                display_stations(filtered_stations)
            else:
                print("No stations found for the given connector type.\n")

        elif choice == '4':
            station_name = input("Enter the name of the station to book a slot: ")
            book_slot(station_name)

        elif choice == '5':
            print("Thank you for using the EV Charging Station Finder and Slot Booking System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.\n")

main()