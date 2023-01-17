import os 

print("Welcome to Data Generator!")
os.system('python3 data_generator.py')

a = int(input('Please type 1 for csv_gnerator.py or type 2 for json_writer.py: '))  

if(a == 1):
    print('You picked csv_generator, please wait a second')
    os.system('python3 csv_generator.py')
    print('Finished please find data.csv in this current directory as data.csv')
elif(a == 2):
    print('You pick json_writer, please wait a second')
    os.system('python3 json_writer.py')
    print('Finished please find data.json in this in this current directory as data.json')
else: 
    print('Just start over')

