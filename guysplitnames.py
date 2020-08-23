import csv
ln = open("lastNames.txt", "w")
f = open("womenlastName.txt", "r")
fl = open("menlastName.txt", "r")
content = f.read()
content_list = content.splitlines()
count = len(content_list)

last_name_list = []
second_last_name_list = []
for x in content_list:
	last_name_list.append(x)
for x in content_list:
    second_last_name_list.append(x)
    
for w in range(0, count-1):
    name = last_name_list[w].split(",")
    fn = open("lastNames.txt", "a")
    fn.write (name[0] + "\n")
    name = second_last_name_list[w].split(",")
    fl = open("lastNames.txt", "a")
    fl.write(name[0] + "\n") 