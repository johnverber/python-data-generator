import sys
import random
import csv

#files to read from 
data_read = open('data.txt', 'r')

#process data and write to csv file
with open('data.csv', 'w', newline='') as f:
	thewriter = csv.writer(f)

	thewriter.writerow(['Last', 'First', 'Email', 'Address', 'Phone'])
