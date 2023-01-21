#Find the position vector of the mid point of the vector joining the points P(2, 3, 4) and Q(4, 1, –2).

import numpy as np

p = np.array([2.0,3.0,4.0])
q = np.array([4.0,1.0,-2.0])

#mid point of the vector joining the points P and Q
m = (p+q)/2
print("Mid point of the vector joining the points P and Q is", m)