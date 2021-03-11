# Paul Christman (Student ID: 001524778)
import csv
from HashTable import HashMap

with open('package_data.csv') as file:
    csv_reader = csv.reader(file, delimiter=",")

    hash_map = HashMap()  # Creates an instance of the Hash Map class
    first_truck = []  # A list that represents the first truck's deliveries
    second_truck = []  # A list that represents the second truck's deliveries
    third_truck = []  # A list that represents the third truck's deliveries

    # Reads in values from a CSV file and inserts them into key / value pairs
    # Space-time complexity of O(N)
    for element in csv_reader:
        package_id = element[0]
        address = element[1]
        city = element[2]
        state = element[3]
        zip_code = element[4]
        delivery = element[5]
        size = element[6]
        note = element[7]
        delivery_start = ''
        address_location = ''
        delivery_status = "At hub"

        value = [package_id, address_location, address, city, state, zip_code, delivery, size, note,
                 delivery_start, delivery_status]

        # Applies conditional statements on packages
        # This sorts the ones with special criteria

        # Correcting the wrong address package
        if '84101' in value[5] and '10:30' not in value[6]:
            third_truck.append(value)
        if 'Wrong address listed' in value[8]:
            value[2] = '410 S State St'
            value[5] = '84111'
            third_truck.append(value)

        # Load the first delivery
        if value[6] != 'EOD':
            if 'Must' in value[8] or 'None' in value[8]:
                first_truck.append(value)
        if value[0] == '19':
            first_truck.append(value)

        # Second truck's deliveries
        if 'Can only be' in value[8]:
            second_truck.append(value)
        if 'Delayed' in value[8]:
            second_truck.append(value)

        # Check remaining packages
        if value not in first_truck and value not in second_truck and value not in third_truck:
            if len(second_truck) > len(third_truck):
                third_truck.append(value)
            else:
                second_truck.append(value)

        # Insert the items into the hash table
        hash_map.insert(package_id, value)

    # Shows the packages loaded in the first truck
    # Space-time complexity is O(1)
    def check_first():
        return first_truck

    # Shows the package loaded in the second truck
    # Space-time complexity is O(1)
    def check_second():
        return second_truck

    # Shows the packages loaded in the third truck
    # Space-time complexity is O(1)
    def check_third():
        return third_truck

    # Shows the full list of packages
    # Space_time complexity is O(1)
    def check_hash():
        return hash_map
