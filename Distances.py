# Paul Christman (Student ID: 001524778)
import csv
import datetime

# I split the Distance Table into two different csv files by hand because I felt it was easier to work with
with open("distance_data.csv") as distance_csv:
    distance_file = list(csv.reader(distance_csv, delimiter=","))
with open("address_data.csv") as address_csv:
    address_file = list(csv.reader(address_csv, delimiter=","))


# Returns the list of addresses
# Space-time complexity is O(N)
def get_address():
    return address_file


# Calculates the distance for the trucks
# Space-time complexity of O(1)
def get_distance(row, col, total):
    distance = distance_file[row][col]
    if distance == '':
        distance = distance_file[col][row]
    return total + float(distance)


# Calculates current distance based on row/col pairs
# Space-time complexity of O(1)
def get_current(row, col):
    distance = distance_file[row][col]
    if distance == '':
        distance = distance_file[col][row]
    return float(distance)


# These are the times that the trucks leave the hub
first_time = ['8:00:00']
second_time = ["09:10:00"]
third_time = ["11:00:00"]


# The following functions calculates the current time for each truck
# Space-time complexity for each is O(N)
def check_time_first(distance):
    new_time = distance / 18
    distance_in_minutes = '{0:02.0f}:{1:02.0f}'.format(*divmod(new_time * 60, 60))
    final_time = distance_in_minutes + ':00'
    first_time.append(final_time)
    total = datetime.timedelta()
    for i in first_time:
        (hrs, mins, sec) = i.split(':')
        total += datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(sec))
    return total


# Repeated function for second truck
def check_time_second(distance):
    new_time = distance / 18
    distance_in_minutes = '{0:02.0f}:{1:02.0f}'.format(*divmod(new_time * 60, 60))
    final_time = distance_in_minutes + ':00'
    second_time.append(final_time)
    total = datetime.timedelta()
    for i in second_time:
        (hrs, mins, sec) = i.split(':')
        total += datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(sec))
    return total


# Repeated function for third truck
def check_time_third(distance):
    new_time = distance / 18
    distance_in_minutes = '{0:02.0f}:{1:02.0f}'.format(*divmod(new_time * 60, 60))
    final_time = distance_in_minutes + ':00'
    third_time.append(final_time)
    total = datetime.timedelta()
    for i in third_time:
        (hrs, mins, sec) = i.split(':')
        total += datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(sec))
    return total


first_optimized = []
first_optimized_index = []
second_optimized = []
second_optimized_index = []
third_optimized = []
third_optimized_index = []


# This is my sorting algorithm that follows the greedy approached.
# It uses a recursive call to determine the best location to visit next based
# on the current location

# It has three parameters: A list of the packages, the truck number,
# and the current location of the truck

# The first for loop finds the shortest distance to the next delivery.
# The lowest value will consistently change until the minimum value
# is found

# The second for loop determines what happens whe the minimum value has
# been assigned to lowest_val. Conditional statements are conducted
# to see which truck the package is associated with. Values are appended to the
# the appropriate truck lists. The current package is then popped out the list
# and the location moves to the next location that is optimal. Then a recursive
# call is conducted for the next location and the updated, shorter list. The
# process continues until the base case is called, and the function returns the
# now empty list. The base case is if the length of the list is 0 or None.

# Space-Time Complexity is O(N^2)

def shortest_route(package_list, truck_num, curr_loc):
    if len(package_list) == 0:
        return package_list

    lowest_val = 50
    location = 0
    try:
        for i in package_list:
            value = int(i[1])
            if get_current(curr_loc, value) <= lowest_val:
                lowest_val = get_current(curr_loc, value)
                location = value
        for i in package_list:
            value = int(i[1])
            if get_current(curr_loc, value) == lowest_val:
                if truck_num == 1:
                    first_optimized.append(i)
                    first_optimized_index.append(i[1])
                    package_list.pop(package_list.index(i))
                    curr_loc = location
                    shortest_route(package_list, 1, curr_loc)
                elif truck_num == 2:
                    second_optimized.append(i)
                    second_optimized_index.append(i[1])
                    package_list.pop(package_list.index(i))
                    curr_loc = location
                    shortest_route(package_list, 2, curr_loc)
                elif truck_num == 3:
                    third_optimized.append(i)
                    third_optimized_index.append(i[1])
                    package_list.pop(package_list.index(i))
                    curr_loc = location
                    shortest_route(package_list, 3, curr_loc)
    except IndexError:
        pass


first_optimized_index.insert(0, '0')
second_optimized_index.insert(0, '0')
third_optimized_index.insert(0, '0')


# All of the following functions are just designed to return a value
# All have the Space-Time Complexity of O(1)
def first_truck():
    return first_optimized


def first_index():
    return first_optimized_index


def second_truck():
    return second_optimized


def second_index():
    return second_optimized_index


def third_truck():
    return third_optimized


def third_index():
    return third_optimized_index
