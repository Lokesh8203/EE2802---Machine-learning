#Find the slope of the line, which makes an angle of 30° with the positive direction of y -axis measured anticlockwise.

import numpy as np

#direction vector of y axis
y = np.array([0,1])

l1 = np.array([1,np.tan(2*np.pi/3)])
l2 = np.array([1,np.tan(2*np.pi/3)])
print(np.tan(2*np.pi/3))

#Angle between the line and y axis
theta = np.arccos(np.dot(y,l)/(np.linalg.norm(y)*np.linalg.norm(l)))
theta = theta*180/np.pi

print("Angle between the line and y axis is", theta)