# To Do:
    # Label the arrays, ant follower, leader, etc
    # This is not ver DRY, things repeat too much, but it makes some sense
    # Perhaps, if there are more tracks, 10, 20+, I can have a loop which creates
    # an np.array for every tracking file. I've seen this before Udacity


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


f2 = open('track_00000002.txt', 'r')
f2.next() # lets skip the header
my_list2 = list()
counter2 = 0
for line2 in f2:
    counter2 = counter2 + 1
f2.close

# This 2000 here needs to be dynamic. It needs to be the size of the lines in the file
soa2 = np.zeros(shape=(counter2,2))
counter2 = 0
i2 = 0;

f2 = open('track_00000002.txt', 'r')
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

################################################################################

plt.figure()
ax = plt.gca()
# This needs to be dynamic. How can read in the array and find the min and max?
ax.set_xlim([80, 200])
ax.set_ylim([80, 200])

def update(val):

    ax.clear()
    i = int(round(sfreq.val))
    # i-1 for bounds check. Doesnt work
    if i-1 < len(soa):
        X, Y = soa[i]
        U, V = soa[i+1]
        ax.annotate("", xy=(U, V), xytext=(X, Y),
                arrowprops=dict(arrowstyle="->", color='red'))
    if i-1 < len(soa2):
        A, B = soa2[i]
        C, D = soa2[i+1]
        ax.annotate("", xy=(C, D), xytext=(A, B),
            arrowprops=dict(arrowstyle="->"))

axfreq = plt.axes([0.25, 0.03, 0.65, 0.03])
# This needs to be fixed to make it choose the bigger one
sfreq = Slider(axfreq, 'Next', 0, len(soa2), valinit=0)
sfreq.on_changed(update)

plt.show()
