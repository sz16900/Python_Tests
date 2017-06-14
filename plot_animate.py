# To Do:
    # I need to remove the arrows once I click
    # Sliders for faster lookup
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

# This 2000 here needs to be dynamic. It needs to be the size of the lines in the file
soa = np.zeros(shape=(2000,2))
i = 0;

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

# This 2000 here needs to be dynamic. It needs to be the size of the lines in the file
soa2 = np.zeros(shape=(2000,2))
i2 = 0;

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

# This needs to be better because I may not want it to start off right away.

# A, B, C, D = soa2[0]
# ax.annotate("", xy=(X, Y), xytext=(U, V),
#     arrowprops=dict(arrowstyle="->"))
# ax.annotate("", xy=(A, B), xytext=(C, D),
#     arrowprops=dict(arrowstyle="->"))
# plt.draw()


class Index(object):
    ind = 0

    def next(self, event):
        i = self.ind
        X, Y = soa[i]
        A, B =soa2[i]

        self.ind += 1
        i = self.ind
        U, V = soa[i]
        C, D  = soa2[i]

        # Remember that the tail is xytext
        ax.annotate("", xy=(U, V), xytext=(X, Y),
            arrowprops=dict(arrowstyle="->", color='red'))
        ax.annotate("", xy=(C, D), xytext=(A, B),
            arrowprops=dict(arrowstyle="->"))
        plt.draw()

    def prev(self, event):
        self.ind -= 1
        i = self.ind
        X, Y, U, V = soa[i]
        A, B, C, D = soa2[i]
        ax.annotate("", xy=(X, Y), xytext=(U, V),
            arrowprops=dict(arrowstyle="->"))
        ax.annotate("", xy=(A, B), xytext=(C, D),
            arrowprops=dict(arrowstyle="->"))
        plt.draw()

callback = Index()
# axprev = plt.axes([0.7, 0.05, 0.1, 0.075])
# axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
# bnext = Button(axnext, 'Next')
# bnext.on_clicked(callback.next)
# bprev = Button(axprev, 'Previous')
# bprev.on_clicked(callback.prev)

def update(val):
    # amp = samp.val
    ax.clear()

    i = int(round(sfreq.val))
    X, Y = soa[i]
    U, V = soa[i+1]
    A, B = soa2[i]
    C, D = soa2[i+1]
    ax.annotate("", xy=(U, V), xytext=(X, Y),
            arrowprops=dict(arrowstyle="->", color='red'))
    ax.annotate("", xy=(C, D), xytext=(A, B),
        arrowprops=dict(arrowstyle="->"))

axfreq = plt.axes([0.25, 0.03, 0.65, 0.03])
sfreq = Slider(axfreq, 'Next', 0, 200, valinit=0)
sfreq.on_changed(update)

print soa[115]
plt.show()
