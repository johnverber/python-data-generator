import sys
import random
import csv

#read files
female_done = open('female_done.txt', 'r')
male_done = open('male_done.txt', 'r')
phone = open('phone.txt', 'r')
street = open('address.txt', 'r')

#write files
data = open('data.txt', 'w')

#class for user input exceptions
class Error(Exception):
	"""Base class for other exceptions"""
	pass

class ValueTooSmall(Error):
	"""Raised when the input value is too small"""
	pass

class ValueTooLarge(Error):
	"""Raise when input value is too large"""
	pass

#check if using arguments
if len(sys.argv) == 2:
	num = int(sys.argv[1])

#no arguments ask for number of data
else:
	while True:
		try:
			answer = True
			num = input("Please enter a number between 1-1000: ")
			num = int(num)
			if(num > 1000):
				raise ValueTooLarge
		
			elif(num < 1):
				raise ValueTooSmall

			break
		except ValueError:
			print("Please enter a valid interger! Please try again...")
		except ValueTooSmall:
			print("Your number is too small, must be greater than 0! Please try again...")
		except ValueTooLarge:
			print("Your number is too large, must be less than 1001! Please try again...")

#pull in data from files into separate lists
girl_list = []
for x in female_done:
	girl_list.append(x)

boy_list = []
for x in male_done:
	boy_list.append(x)

phone_list = []
for x in phone:
	phone_list.append(x)

street_list = [] 
for x in street:
	street_list.append(x)

#process data to txt file 

ext = ['@hotmail.com', '@gmail.com', '@yahoo.com', '@whatever.com']

for x in range(0, num):
	rand_gender = random.randint(0,1) #this is for randomizing the number of male/females
	if rand_gender == 1:
		name = girl_list[x].split(",")
		email = name[1].strip() + '.' + name[0].strip() + ext[random.randint(0,3)].strip()
		address = street_list[x].strip()
		ph_num = phone_list[x].strip()
		data.write(girl_list[x].strip() + ',' + email + ',' + address + ',' + ph_num + '\n')
	elif rand_gender == 0:
		name = boy_list[x].split(",")
		email = name[1].strip() + '.' + name[0].strip() + ext[random.randint(0,3)].strip()
		address = street_list[x].strip()
		ph_num = phone_list[x].strip()
		data.write(girl_list[x].strip() + ',' + email + ',' + address + ',' + ph_num + '\n')

print("finished!")

#choose to print out in csv or json
"""def printData():
	answer = input('Please choose 1 for csv or 2 for json output file: ')
	if(answer == '1'):
		#csv_generator.csv_write('/Users/johnverber/Documents/GitHub/python-data-generator/data.txt','/Users/johnverber/Documents/GitHub/python-data-generator/data.csv')
		data_read = open('data.txt', 'r')

		#process data and write to csv file
		with open('data.csv', 'w', newline='') as f:
			thewriter = csv.writer(f)

			#thewriter.writerow(['Last', 'First', 'Email', 'Address', 'Phone'])
			for x in data_read:
				y = x.split(',')
				thewriter.writerow([y[0].strip(), y[1].strip(), y[2].strip(), y[3].strip(), y[4].strip()])
	elif(answer == '2'):
		#files to read from 
		data_read = open('data.txt', 'r')
		print(data_read)

		#process data and write to json file
		for x in data_read:
			y = x.split(',')
			
			json_data = {"First" : y[0].strip(), "Last" : y[1].strip(), "Email" : y[2].strip(), "Address" : y[3].strip(), "Phone" : y[4].strip() }
			
			with open('data.json', 'a') as f:
				data = json.dumps(json_data, sort_keys=True, indent=4 * ' ')
				f.write(data + '\n')
	else:
		printData()

printData()"""


