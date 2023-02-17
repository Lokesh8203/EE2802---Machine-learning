#Find the coordinates of the focii, the vertices, the length of major and minor axes, the eccentricity and the length of the latus rectum of an ellipse whose equation is given by (x^2)/36 + (y^2)/49 = 1

import numpy as np

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