#find the equation of the line which satisfy the given conditions: Intersecting the y-axis at a distance of 2 units above the origin and making an angle of pi/6 with positive direction of the x-axis.

import numpy as np

omat = np.array([[0, -1], [1, 0]])

d = np.array([1, np.tan(np.pi/6)])
n = omat@d

a = np.array([0, 2])

print("The equation of the line is: ", n, "x = ", n@a)