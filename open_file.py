import numpy as np

f = open('track_00000001.txt', 'r')
f.next() # lets skip the header
my_list = list()
counter = 0

# This 200 here needs to be dynamic. It needs to be the size of the lines in the file
a = np.zeros(shape=(2000,2))
i = 0;

for line in f:
    counter = counter + 1
    intList = map(float, line.strip().split())
    my_list.append(intList[1])
    my_list.append(intList[2])
    a[i] = my_list
    i = i + 1
    del my_list[:]

print type(a)
print a
f.close()
