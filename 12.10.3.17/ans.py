#Show that the vectors A = [2,-1, 1], B = [1, -3, -5] and C = [3,-4, -4] form the vertices of a right angled triangle.

import numpy as np

a = np.array([2,-1,1])
b = np.array([1,-3,-5])
c = np.array([3,-4,-4])

#Vectors of sides of triangle
A = a-b
B = b-c
C = c-a

#area of triangle from abouve vectors is
area = 1/2*(np.linalg.norm(np.cross(A,B)))


#Check if the vectors form a right angled triangle
if (area != 0) and (np.dot(A,B) == 0) or (np.dot(B,C) == 0) or (np.dot(C,A) == 0):
    print("The vectors form a right angled triangle")
else:
    print("The vectors do not form a right angled triangle")