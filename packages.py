# Paul Christman (Student ID: 001524778)
import datetime
import Distances
import CsvReader

first_delivery = []
second_delivery = []
third_delivery = []
first_distance = []
second_distance = []
third_distance = []

first_time = ['8:00:00']
second_time = ['9:10:00']
third_time = ['11:00:00']

# This sets the delivery start time to 8 AM for all of truck one's packages
# Space-time complexity of O(N)
for index, value in enumerate(CsvReader.check_first()):
    CsvReader.check_first()[index][9] = first_time[0]
    first_delivery.append(CsvReader.check_first()[index])

# This compares truck one's addresses to the addresses in the address list
# Space-time complexity of O(N^2)
for index, outside in enumerate(first_delivery):
    for inside in Distances.get_address():
        if outside[2] == inside[2]:
            first_distance.append(outside[0])
            first_delivery[index][1] = inside[0]

Distances.shortest_route(first_delivery, 1, 0)
first_total = 0

# This calculates the total distance of the first truck and the distance and time of each package
# Space-time complexity of O(N)
for index in range(len(Distances.first_index())):
    try:
        first_total = Distances.get_distance(int(Distances.first_index()[index]),
                                             int(Distances.first_index()[index + 1]), first_total)
        del_pack = Distances.check_time_first(Distances.get_current(int(Distances.first_index()[index]),
                                                                    int(Distances.first_index()[index + 1])))
        Distances.first_truck()[index][10] = str(del_pack)
        CsvReader.check_hash().update(int(Distances.first_truck()[index][0]), first_delivery)
    except IndexError:
        pass

# This sets the delivery start time to 9:10 AM for all of truck two's packages
# Space-time complexity of O(N)
for index, value in enumerate(CsvReader.check_second()):
    CsvReader.check_second()[index][9] = second_time[0]
    second_delivery.append(CsvReader.check_second()[index])

# This compares truck two's addresses to the addresses in the address list
# Space-time complexity of O(N^2)
for index, outside in enumerate(second_delivery):
    for inside in Distances.get_address():
        if outside[2] == inside[2]:
            second_distance.append(outside[0])
            second_delivery[index][1] = inside[0]

Distances.shortest_route(second_delivery, 2, 0)
second_total = 0

# This calculates the total distance of the second truck and the distance and time of each package
# Space-time complexity of O(N)
for index in range(len(Distances.second_index())):
    try:
        second_total = Distances.get_distance(int(Distances.second_index()[index]),
                                              int(Distances.second_index()[index + 1]), second_total)
        del_pack = Distances.check_time_second(Distances.get_current(int(Distances.second_index()[index]),
                                                                     int(Distances.second_index()[index + 1])))
        Distances.second_truck()[index][10] = str(del_pack)
        CsvReader.check_hash().update(int(Distances.second_truck()[index][0]), second_delivery)
    except IndexError:
        pass

# This sets the delivery start time to 11 AM for all of truck three's packages
# Space-time complexity of O(N)
for index, value in enumerate(CsvReader.check_third()):
    CsvReader.check_third()[index][9] = third_time[0]
    third_delivery.append(CsvReader.check_third()[index])

# This compares truck three's addresses to the addresses in the address list
# Space-time complexity of O(N^2)
for index, outside in enumerate(third_delivery):
    for inside in Distances.get_address():
        if outside[2] == inside[2]:
            third_distance.append(outside[0])
            third_delivery[index][1] = inside[0]

Distances.shortest_route(third_delivery, 3, 0)
third_total = 0

# This calculates the total distance of the third truck and the distance and time of each package
# Space-time complexity of O(N)
for index in range(len(Distances.third_index())):
    try:
        third_total = Distances.get_distance(int(Distances.third_index()[index]),
                                             int(Distances.third_index()[index + 1]), third_total)
        del_pack = Distances.check_time_third(Distances.get_current(int(Distances.third_index()[index]),
                                                                    int(Distances.third_index()[index + 1])))
        Distances.third_truck()[index][10] = str(del_pack)
        CsvReader.check_hash().update(int(Distances.third_truck()[index][0]), third_delivery)
    except IndexError:
        pass


# This returns the total distance of all three trucks combined
# Space-time complexity of O(1)
def total_distance():
    return first_total + second_total + third_total
