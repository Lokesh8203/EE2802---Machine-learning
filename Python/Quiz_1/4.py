#Find the area of a triangle whose vertcies are (-5,-1), (3,-5), and (5,2)

import numpy as np

A = np.array([-5, -1])
B = np.array([3, -5])
C = np.array([5, 2])

area = 0.5 * np.linalg.norm(np.cross(B-A, C-A))
print(area)