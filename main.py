# Author: Jacob Wallace
# Student Id: 009925162

import datetime
import time
from Delivery import deliverPackages, getAllPackageStatus, getSinglePackageStatus, loadTruck
from Truck import Truck

def main():
    #intializing 3 truck classes and manually loading the package id's for each route
    truck1 = Truck(1, 18, 0, 16, [1, 19, 20, 21, 34, 37, 40, 11, 29, 3, 14, 15, 16, 13], 0, '4001 S 700 E', datetime.timedelta(hours=8))
    truck2 = Truck(2, 18, 0, 16, [6, 30, 31, 4, 3, 12, 38, 39, 27, 35, 36, 18, 22, 23, 24, 26], 0, '4001 S 700 E', datetime.timedelta(hours=9, minutes=5))
    truck3 = Truck(3, 18, 0, 16, [2, 5, 7, 8, 32, 33, 28, 25, 10, 9, 17], 0, '4001 S 700 E', datetime.timedelta(hours=10, minutes=20)) 

    # load each truck with packages
    print('Loading trucks...\n')
    time.sleep(.5)
    loadTruck(truck1)
    loadTruck(truck2)
    loadTruck(truck3)


    # determine the best route for each truck and deliver packages
    print('Delivering Packages...\n')
    time.sleep(.5)
    deliverPackages(truck1)
    deliverPackages(truck2)
    deliverPackages(truck3)

    # print the total mileage of the route
    print('Total Mileage: ', round(truck1.mileage + truck2.mileage + truck3.mileage, 2), 'miles')
    print('--------------------')
    print('Truck 1: ', round(truck1.mileage, 2), 'miles')
    print('Truck 2: ', round(truck2.mileage, 2), 'miles')
    print('Truck 3: ', round(truck3.mileage, 2), 'miles')

    # get user input for package and time in question
    inputId = input('\nPlease enter a package ID number to see its status, or type "all" to see all packages: ')
    inputTime = input('Enter a time you would like to see the status for HH:MM: ')

    # validate user input and display correct package status 
    if inputId.upper() == ('ALL'):
        try:
            h, m = inputTime.split(':')
            lookupTime = datetime.timedelta(hours=int(h), minutes=int(m))
            getAllPackageStatus(lookupTime)
        except Exception:
            print('Invalid input.  Please enter a valid package ID and ensure the time is in this format HH:MM')
            exit()
    else:
        try: 
            h, m = inputTime.split(':')
            lookupTime = datetime.timedelta(hours=int(h), minutes=int(m))
            getSinglePackageStatus(int(inputId), lookupTime)
        except Exception:
            print('Invalid input.  Please enter a valid package ID and ensure the time is in this format HH:MM')
            exit()

main()