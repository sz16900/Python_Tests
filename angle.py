import math

angle = math.atan2(97.0659, 97.686) - math.atan2(81.875, 88.1583)

if angle < 0:
    angle += 2 * 3.1416

print angle
