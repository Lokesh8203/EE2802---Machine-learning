#Find the coordinates of point A, where AB is diameter of a circle whose center is (2,-3), B = (1,4)
import numpy as np

B = np.array([1,4])
Center = np.array([2,-3])

A = 2*Center - B
print(A)