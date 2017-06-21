import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, Slider

#####################################Read File##################################

f = open('track_00000001.txt', 'r')
f.next() # lets skip the header
my_list = list()
counter = 0
for line in f:
    counter = counter + 1
f.close

followerAnt = np.zeros(shape=(counter,2))
counter = 0
i = 0;

f = open('track_00000001.txt', 'r')
f.next() # lets skip the header
for line in f:
    counter = counter + 1
    intList = map(float, line.strip().split())
    my_list.append(intList[1])
    my_list.append(intList[2])
    followerAnt[i] = my_list
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

leaderAnt = np.zeros(shape=(counter2,2))
counter2 = 0
i2 = 0;

f2 = open('track_00000000.txt', 'r')
f2.next() # lets skip the header
for line2 in f2:
    counter2 = counter2 + 1
    intList2 = map(float, line2.strip().split())
    my_list2.append(intList2[1])
    my_list2.append(intList2[2])
    leaderAnt[i2] = my_list2
    i2 = i2 + 1
    del my_list2[:]
f.close()

#########################Get Siingle Angle From Lines###########################

# def dot(vA, vB):
#     return vA[0]*vB[0]+vA[1]*vB[1]
# def ang(lineA, lineB):
#     # Get nicer vector form
#     vA = [(lineA[0][0]-lineA[1][0]), (lineA[0][1]-lineA[1][1])]
#     vB = [(lineB[0][0]-lineB[1][0]), (lineB[0][1]-lineB[1][1])]
#     # Get dot prod
#     dot_prod = dot(vA, vB)
#     # Get magnitudes
#     magA = dot(vA, vA)**0.5
#     magB = dot(vB, vB)**0.5
#     # Get cosine value
#     cos_ = dot_prod/magA/magB
#     # Get angle in radians and then convert to degrees
#     angle = math.acos(dot_prod/magB/magA)
#     # Basically doing angle <- angle mod 360
#     ang_deg = math.degrees(angle)%360
#
#     if ang_deg-180>=0:
#         # As in if statement
#         return 360 - ang_deg
#     else:
#
#         return ang_deg

def ang(P1X,P1Y,P2X,P2Y,P3X,P3Y):
    numerator = P2Y*(P1X-P3X) + P1Y*(P3X-P2X) + P3Y*(P2X-P1X)
    denominator = (P2X-P1X)*(P1X-P3X) + (P2Y-P1Y)*(P1Y-P3Y)
    ratio = numerator/denominator
    angleRad = math.atan(ratio);
    angleDeg = (angleRad*180)/3.1416;
    if angleDeg<0:
        angleDeg = 180+angleDeg
        return angleDeg

#########################Produce Angles#########################################

arrayOfFifteensFollower = list()
arrayOfFifteensLeader = list()
i = 0
for i in range(0,len(followerAnt), 15):
    # print "Iteration", i # Python is an interesting language (no concat?)
    # print followerAnt[i]
    arrayOfFifteensFollower.append(followerAnt[i])
    arrayOfFifteensLeader.append(leaderAnt[i])

i = 0
arrayOfAngles = list()
for i in range(0, len(arrayOfFifteensLeader)-1):

    arrayOfAngles.append(ang(arrayOfFifteensFollower[i][0], arrayOfFifteensFollower[i][1],
    arrayOfFifteensFollower[i+1][0], arrayOfFifteensFollower[i+1][1],
    arrayOfFifteensLeader[i][0], arrayOfFifteensLeader[i][1]))

# plt.hist(arrayOfAngles)
# plt.show()
print arrayOfAngles
