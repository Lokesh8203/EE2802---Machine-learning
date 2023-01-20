#Find the slope of the line, which makes an angle of 30° with the positive direction of y -axis measured anticlockwise.

import numpy as np
import sympy as sp

#direction vector of y axis
y = np.array([0,1])

#Rotate this direction vector by pi/6 in anticlockwise direction to get the direction vector of the line

#Rotation matrix
R = np.array([[np.cos(np.pi/6), -np.sin(np.pi/6)],[np.sin(np.pi/6), np.cos(np.pi/6)]])
#direction vector of the line
l = R@y

#slope of the line
m = l[1]/l[0]
print("Slope of the line is", m)

