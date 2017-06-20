import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, Slider

f = open('track_00000001.txt', 'r')
f.next() # lets skip the header
my_list = list()
counter = 0
for line in f:
    counter = counter + 1
f.close

soa = np.zeros(shape=(counter,2))
counter = 0
i = 0;

f = open('track_00000001.txt', 'r')
f.next() # lets skip the header
for line in f:
    counter = counter + 1
    intList = map(float, line.strip().split())
    my_list.append(intList[1])
    my_list.append(intList[2])
    soa[i] = my_list
    i = i + 1
    del my_list[:]
f.close()

f2 = open('track_00000000.txt', 'r')
f2.next() # lets skip the header
my_list2 = list()
counter2 = 0
for line2 in f2:
    counter2 = counter2 + 1
f2.close

soa2 = np.zeros(shape=(counter2,2))
counter2 = 0
i2 = 0;

f2 = open('track_00000000.txt', 'r')
f2.next() # lets skip the header
for line2 in f2:
    counter2 = counter2 + 1
    intList2 = map(float, line2.strip().split())
    my_list2.append(intList2[1])
    my_list2.append(intList2[2])
    soa2[i2] = my_list2
    i2 = i2 + 1
    del my_list2[:]
f.close()

i = 0
distance = list()
for i in range(0, len(soa)):
    dist = math.hypot(soa2[i][0] - soa[i][0], soa2[i][1] - soa[i][1])
    distance.append(dist)

bins = [0.0, 5.0]
plt.hist(distance)
plt.show()
