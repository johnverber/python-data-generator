import csv
fn = open("womenfirstName.txt", "w")
f = open("female_done.txt", "r")
fl = open("womenlastName.txt", "w")
ff_name = []
fl_name = []
content = f.read()
content_list = content.splitlines()
count = len(content_list)

girl_list = []
for x in content_list:
	girl_list.append(x)

for w in range(0, count-1):
    name = girl_list[w].split(",")
    fn = open("womenfirstName.txt", "a")
    fn.write (name[1] + "\n")
    fl = open("womenlastName.txt", "a")
    fl.write(name[0] + "\n") 


   
   
