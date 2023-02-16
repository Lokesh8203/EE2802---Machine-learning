#Find the coordinates of the focus, axis of the parabola, the equation of the directrix and the length of the latus rectum y^2 = 10x

import numpy as np

def norm(x):
    return np.sqrt(x[0]*x[0] + x[1]*x[1])

def n(l2, P):
    return np.sqrt(l2)*P[0]

def c(u, l2, f, n):
    return (norm(u)*norm(u) - l2*f)/(2*(np.transpose(u))@n)

def focus(c, e, n, u, l2):
    return (c*e*e*n - u)/(l2)

def l1(V):
    return V[0][0]

def l2(V):
    return V[1][1]

def LR(u, P, l2):
    return (-2*np.transpose(u)@P[0])/(l2)

V = np.array([[0, 0], [0, 1]])
u = np.array([-5, 0])
f = 0
P = np.array([[1, 0], [0, 1]])
e = 1 #parabola

lambda_1 = l1(V)
lambda_2 = l2(V)

n = n(lambda_2, P)
c  = c(u, lambda_2, f, n)

F = focus(c, e, n, u, lambda_2)
Latus_rectum = LR(u, P, lambda_2)

print("The focus of parabola is ", F)
print("The directrix equations is given as", np.transpose(n), 'x = ', c)
print("The lenght of LR of parabola is", Latus_rectum)


