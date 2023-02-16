#Find the coordinates of the focus, axis of the parabola, the equation of the directrix and the length of the latus rectum y^2 = 10x
import numpy as np

def focus(c, e, n, u, w):
    return (c*(e**2)*n - u)/(w[1])

def LR(u, v, w):
    return (-2*(u@v[0]))/(w[1])

V = np.array([[0, 0], [0, 1]])
u = np.array([-5, 0])
f = 0
e = 1 #parabola

w,v = np.linalg.eig(V)
#w eigenvalues
#v eigenvectors

n = np.sqrt(w[1])*v[0]
c = (np.linalg.norm(u)**2 - w[1]*f)/(2*(u@n))

F = focus(c, e, n, u, w)
Latus_rectum = LR(u, v, w)

print("The focus of parabola is ", F)
print("The directrix equations is given as", np.transpose(n), 'x = ', c)
print("The lenght of LR of parabola is", Latus_rectum)


