import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

omat = np.array([[0,1],[-1,0]])

#Generate line points
def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

def line_gen_vector(n, c, x):
    y = (c - n[0]*x)/n[1]
    return y

h = sp.Symbol('h')

#Given points
A  = np.array([h, 3])
B = np.array([4, 1])

#Given line
n = np.array([7, -9])
c = 19

#Slope of given line
m = n@omat

#As its given both lines are perpendicular, so
h = sp.solve(sp.Eq(m@(B-A),0),h)[0]
print(h)

A = np.array([h, 3]) #Redifining A

#Plot the given line
x = np.linspace(-7, 12, 100)

#Plot line formed by A and B
y = line_gen_vector((B-A)@omat, ((B-A)@omat)@A, x)
plt.plot(x, y, label='$(2  14/9)x = 86/9$')

#Plot the given line
y = line_gen_vector(n, c, x)
plt.plot(x, y, label='$(7  -9)x = 19$')

#Plot the points
plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 + 0.1), B[1] * (1 - 0.1) , 'B')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')
plt.savefig('/home/lokesh/EE2802/EE2802-Machine_learning/11.10.3.10/figs/lines.png')