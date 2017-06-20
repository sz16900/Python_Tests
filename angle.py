import math

def dotproduct(v1, v2):
  return sum((a*b) for a, b in zip(v1, v2))

def length(v):
  return math.sqrt(dotproduct(v, v))

# def angle(v1, v2):
print math.acos(dotproduct([97.686, 97.0659], [88.1583, 81.875]) / (length([97.686, 97.0659]) * length([88.1583, 81.875])))
