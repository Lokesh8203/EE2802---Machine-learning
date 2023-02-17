#Find the coordinates of the focii, the vertices, the length of major and minor axes, the eccentricity and the length of the latus rectum of an ellipse whose equation is given by (x^2)/36 + (y^2)/49 = 1

import numpy as np
import matplotlib as plt

#Generating points on an ellipse
def ellipse_gen(a,b):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_ellipse = np.zeros((2,len))
	x_ellipse[0,:] = a*np.cos(theta)
	x_ellipse[1,:] = b*np.sin(theta)
	return x_ellipse

V = np.array([[36, 0], [0, 49]])
u = np.array([0, 0])
f = -1764

w, v =  np.linalg.eig(V)
#w - eigenvalus
#v eigenvector

e = np.sqrt(1 - w[0]/w[1]) #eccentricity

n = np.sqrt(w[1])*v[1]

f_0 = u@np.linalg.inv(V)@u - f

print("The length of major axis is ", 2*abs(np.sqrt(f_0/w[0])))
print("The length of minor axis is ", 2*abs(np.sqrt(f_0/w[1])))

vertex_1 = np.array([np.sqrt(f_0/w[0]), 0])
vertex_2 = np.array([-np.sqrt(f_0/w[0]), 0])
print("The vertices of ellipse are ", vertex_1, vertex_2)

LR = 2*np.sqrt(abs(f_0*w[0]))/w[1] #latusrectum
print("The lenght of latus recturm is ", LR)

a = 6
b = 7
x_ellipse = ellipse_gen(a,b)

plt.plot(x_ellipse[0,:],x_ellipse[1,:],label='$ellipse$')
plt.plot(u[0],u[1],'o')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid() # minor
plt.axis('equal')
plt.savefig('/home/lokesh/EE2802/EE2802-Machine_learning/11.11.3.5/figs/circle.png')