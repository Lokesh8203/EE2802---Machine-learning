#Find the slope of the line, which makes an angle of 30° with the positive direction of y -axis measured anticlockwise.

import numpy as np
import matplotlib.pyplot as plt

#direction vector of y axis
y = np.array([0,1])

#Rotate this direction vector by (2*pi - pi/6) in anticlockwise direction to get the direction vector of the line

#Rotation matrix
R = np.array([[np.cos(11*np.pi/6), -np.sin(11*np.pi/6)],[np.sin(11*np.pi/6), np.cos(11*np.pi/6)]])
#direction vector of the line
l = R@y

#slope of the line
m = l[1]/l[0]
print("Slope of the line is", m)

#Plot
x = np.linspace(-1,1,100)
y = m*x
plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.savefig('/home/lokesh/EE2802/EE2802-Machine_learning/11.10.1.7/figs/line.png')