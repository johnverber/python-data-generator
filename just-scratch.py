

import random

women_first = open('womenfirstName.txt', 'r')


def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)
print(random_line('women_first'))
###woman_first_name = ""
#woman_first_name = random_line('woman_first')
#print(woman_first_name[0])