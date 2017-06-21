# To Do:
    # Label the arrays, ant follower, leader, etc
    # This is not ver DRY, things repeat too much, but it makes some sense


import numpy as np
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

# This is to find the minimun and maximun value to use for graph
xy = np.min(soa, axis=0)
minx = xy[0]
miny = xy[1]
xy = np.max(soa, axis=0)
maxx = xy[0]
maxy = xy[1]

################################################################################

plt.figure()
ax = plt.gca()

ax.set_xlim([minx, maxx])
ax.set_ylim([miny, maxy])

def update(val):

    ax.clear()
    i = int(round(sfreq.val))

    # This needs to be a bit more DRY

    if i > len(soa)-2:
        print "Reached Boundry"
    else:
        X, Y = soa[i]
        U, V = soa[i+1]
        ax.annotate("", xy=(U, V), xytext=(X, Y),
                arrowprops=dict(arrowstyle="->", color='red'))
    if i > len(soa2)-2:
        print "Reached Boundry"
    else:
        A, B = soa2[i]
        C, D = soa2[i+1]
        ax.annotate("", xy=(C, D), xytext=(A, B),
            arrowprops=dict(arrowstyle="->"))

axfreq = plt.axes([0.25, 0.03, 0.65, 0.03])

# Find how big the slider should be
if len(soa) > len(soa2):
    sliderLength = len(soa)
else:
    sliderLength = len(soa2)

sfreq = Slider(axfreq, 'Next', 0, sliderLength, valinit=0)
sfreq.on_changed(update)

plt.show()
