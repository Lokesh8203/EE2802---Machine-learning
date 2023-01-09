#Find the distance between points A and B, A = (-5,7) and B = (-1,3)

import numpy as np

A = np.array([-5,7])
B = np.array([-1,3])
distance = np.linalg.norm(A-B)
print(distance)