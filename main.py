# Paul Christman (Student ID: 001524778)
from CsvReader import check_hash
from packages import total_distance
import datetime


class Main:
    print('*************************************')
    print("Welcome to the WGUPS Routing Program!")
    print('*************************************\n')
    print(f'The route was completed in {total_distance():.2f} miles. \n')

    begin = input("To begin, please type 1 to view delivery status at a given time"
                  " or 2 to search for an individual package: (exit to exit) ")

    # Space-time complexity is O(N)
    while begin != 'exit':

        if begin == '1':
            try:
                package_time = input('Enter a time in the HH:MM:SS format: ')
                (h, m, s) = package_time.split(':')
                convert_user = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

                # Space-time complexity is O(N^2)
                for count in range(1, 41):
                    try:
                        first = check_hash().get_value(str(count))[9]
                        second = check_hash().get_value(str(count))[10]
                        (h, m, s) = first.split(':')
                        convert_first = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                        (h, m, s) = second.split(':')
                        convert_second = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                    except ValueError:
                        pass

                    if convert_first >= convert_user:
                        check_hash().get_value(str(count))[10] = "At Hub"
                        check_hash().get_value(str(count))[9] = 'Leaves at ' + first
                        print('Package ID: ', check_hash().get_value(str(count))[0])
                        print('Required delivery time: ', check_hash().get_value(str(count))[6])
                        print('Truck Status: ', check_hash().get_value(str(count))[9])
                        print('Delivery Status: ', check_hash().get_value(str(count))[10])
                    elif convert_first <= convert_user:
                        if convert_user < convert_second:
                            check_hash().get_value(str(count))[10] = "In transit"
                            check_hash().get_value(str(count))[9] = "Left at " + first
                            print('Package ID: ', check_hash().get_value(str(count))[0])
                            print('Required delivery time: ', check_hash().get_value(str(count))[6])
                            print('Truck Status: ', check_hash().get_value(str(count))[9])
                            print('Delivery Status: ', check_hash().get_value(str(count))[10])
                        else:
                            check_hash().get_value(str(count))[10] = "Delivered at " + second
                            check_hash().get_value(str(count))[9] = "Left at " + first
                            print('Package ID: ', check_hash().get_value(str(count))[0])
                            print('Required delivery time: ', check_hash().get_value(str(count))[6])
                            print('Truck Status: ', check_hash().get_value(str(count))[9])
                            print('Delivery Status: ', check_hash().get_value(str(count))[10])
            except IndexError:
                print(IndexError)
                exit()
            except ValueError:
                print("Invalid entry")
                exit()

        elif begin == '2':

            count = input('Please enter a package ID: ')
            first = check_hash().get_value(str(count))[9]
            second = check_hash().get_value(str(count))[10]
            package_time = input("Enter a time in the HH:MM:SS format: ")
            (h, m, s) = package_time.split(':')
            convert_user = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            (h, m, s) = first.split(':')
            convert_first = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            (h, m, s) = second.split(':')
            convert_second = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

            if convert_first >= convert_user:
                check_hash().get_value(str(count))[10] = "At Hub"
                check_hash().get_value(str(count))[9] = 'Leaves at ' + first
                print('Package ID: ', check_hash().get_value(str(count))[0])
                print('Street Address: ', check_hash().get_value(str(count))[2], check_hash().get_value(str(count))[3],
                      check_hash().get_value(str(count))[4], check_hash().get_value(str(count))[5])
                print('Required delivery time: ', check_hash().get_value(str(count))[6])
                print('Package weight: ', check_hash().get_value(str(count))[7])
                print('Truck Status: ', check_hash().get_value(str(count))[9])
                print('Delivery Status: ', check_hash().get_value(str(count))[10])
            elif convert_first <= convert_user:
                if convert_user < convert_second:
                    check_hash().get_value(str(count))[10] = "In transit"
                    check_hash().get_value(str(count))[9] = "Left at" + first
                    print('Package ID: ', check_hash().get_value(str(count))[0])
                    print('Street Address: ', check_hash().get_value(str(count))[2],
                          check_hash().get_value(str(count))[3],
                          check_hash().get_value(str(count))[4], check_hash().get_value(str(count))[5])
                    print('Required delivery time: ', check_hash().get_value(str(count))[6])
                    print('Package weight: ', check_hash().get_value(str(count))[7])
                    print('Truck Status: ', check_hash().get_value(str(count))[9])
                    print('Delivery Status: ', check_hash().get_value(str(count))[10])
                else:
                    check_hash().get_value(str(count))[10] = "Delivered at" + second
                    check_hash().get_value(str(count))[9] = "Left at " + first
                    print('Package ID: ', check_hash().get_value(str(count))[0])
                    print('Street Address: ', check_hash().get_value(str(count))[2],
                          check_hash().get_value(str(count))[3],
                          check_hash().get_value(str(count))[4], check_hash().get_value(str(count))[5])
                    print('Required delivery time: ', check_hash().get_value(str(count))[6])
                    print('Package weight: ', check_hash().get_value(str(count))[7])
                    print('Truck Status: ', check_hash().get_value(str(count))[9])
                    print('Delivery Status: ', check_hash().get_value(str(count))[10])
        elif begin == 'exit':
            exit()
        else:
            print('Invalid entry!')
            exit()
