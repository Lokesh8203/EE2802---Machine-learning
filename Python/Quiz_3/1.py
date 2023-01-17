import numpy as np
from numpy.linalg import inv, norm

p1 = np.array([4.0,1.0])
p2 = np.array([6.0,5.0])

n = np.array([4.0,1.0])
c = 16.0

p = np.array([1.0])
q = np.array([0.0])
A = np.vstack((np.hstack((p1*2,p)), np.hstack((p2*2,p)), np.hstack((-n,q))))
B = np.array([[-pow(norm(p1),2)],[-pow(norm(p2),2)],[c]])
x = inv(A)@(B)

#Coordinates of center of circle
print("Center of circle is", x[0][0], x[1][0])
print("Radius of circle is", pow((pow(norm(x[0:2]),2)-x[2][0]), 1/2))