import sys
import math
import csv_writer_module2
import json_writer_module

from faker import Faker

data = open("data.txt", "w")

#class for user input exceptions
"""class Error(Exception):
    #Base class for other exceptions
    pass

class ValueTooSmall(Error):
    #Raised when the input value is too small
    pass

class ValueTooLarge(Error):
    #Raise when input value is too large
    pass"""

def requestNum():
    while True:
        try:
            answer = True
            num = input("Please enter a number between 1-1000: ")
            num = int(num)
            if(num > 1000):
                raise ValueTooLarge

            elif(num < 1):
                raise ValueTooSmall
            else:
                return num
            
        except ValueError:
            print("Please enter a valid interger! Please try again...")
        except ValueTooSmall:
            print("Your number is too small, must be greater than 0! Please try again...")
        except ValueTooLarge:
            print("Your number is too large, must be less than 1001! Please try again...")
        
#check if using arguments
if len(sys.argv) == 2:
    argInput = int(sys.argv[1]) #get number of data points
    try:
        num = int(argInput)#check if input is an integer
        print("Input is an integer")
    except ValueError:#if not an integer, ask for input
        print("Input is not an integer")
        num = requestNum()#get number of data points
else:
    #get number of data points
    num = requestNum()#get number of data points

for x in range(0, num):
    fake = Faker()
    name = fake.name().strip()
    address = fake.address().strip()
    phone = fake.phone_number().strip()
    email = fake.email().strip()
    ss  = fake.ssn().strip()
    print(name + "," + address + "," + phone + "," + email + "," + ss + "\n")
    data.write(name + "," + address + "," + phone + "," + email + "," + ss + "\n")



data.close()
print('Data collection finished!')
#choose to print out in csv or json
def printData():
    answer = input('Please choose 1 for csv or 2 for json output file: ')
    if(answer == '1'):
        csv_writer_module2.csv_run()
        print('Please find your data in "data.csv" in the cwd!!!')
                
    elif(answer == '2'):
        json_writer_module.json_run()
        print('Please find your data in "data.json" in the cwd!!!')
    else:
        printData()

printData()

print("printing all finished!!!")

