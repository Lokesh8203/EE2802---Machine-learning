#Show that the vectors A = [2,-1, 1], B = [1, -3, -5] and C = [3,-4, -4] form the vertices of a right angled triangle.

import numpy as np

a = np.array([2,-1,1])
b = np.array([1,-3,-5])
c = np.array([3,-4,-4])

one_row = np.array([1,1,1])

#rank of the matrix method to check if points form a triangle
if np.linalg.matrix_rank(np.array([a,b,c,one_row])) == 3:
    print("The vectors form a triangle")
else:
    print("The vectors do not form a triangle")

A = a - b
B = b - c
C = c - a

#Check if the vectors form a right angled triangle
if (A@B == 0) or (B@C == 0) or (C@A == 0):
    print("The vectors form a right angled triangle")
else:
    print("The vectors do not form a right angled triangle")
