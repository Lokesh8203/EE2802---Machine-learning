import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from sympy import *

def norm(A):
  #A is sp.matrix
  return sp.sqrt(A[0]*A[0] + A[1]*A[1])

theta = sp.Symbol('theta')
P = sp.Matrix([sp.cos(theta), sp.sin(theta)])
Q = sp.Matrix([sp.cos(sp.pi*1/6), sp.sin(sp.pi*1/6)])
R = sp.Matrix([1, 0])

PQ = P - Q
RQ = R - Q

theta = sp.solve(sp.Eq(sp.simplify((PQ.dot(RQ))/(norm(PQ)*norm(RQ))) - np.cos(np.pi*5/9)), theta)[0]
P = sp.Matrix([sp.cos(theta), sp.sin(theta)])

def circ_gen(O,r):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ.T + O).T
	return x_circ

def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

O = np.array([0,0])
x_circ = circ_gen(O,1)
plt.plot(x_circ[0,:],x_circ[1,:],label='$circle$')

x_PQ = line_gen(P,Q)
plt.plot(x_PQ[0,:],x_PQ[1,:],label='$PQ$')

x_QR = line_gen(Q,R)
plt.plot(x_QR[0,:],x_QR[1,:],label='$QR$')

x_PR = line_gen(P,R)
plt.plot(x_PR[0,:],x_PR[1,:],label='$PR$')

O = sp.Matrix([0, 0])

x_OR = line_gen(O,R)
plt.plot(x_OR[0,:],x_OR[1,:],label='$OR$')

x_OP = line_gen(O,P)
plt.plot(x_OP[0,:],x_OP[1,:],label='$OP$')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

plt.plot(P[0], P[1], 'o')
plt.text(P[0] * (1 + 0.1), P[1] * (1 - 0.1) , 'P')
plt.plot(Q[0], Q[1], 'o')
plt.text(Q[0] * (1 + 0.1), Q[1] * (1 - 0.1) , 'Q')
plt.plot(R[0], R[1], 'o')
plt.text(R[0] * (1 + 0.1), R[1] * (1 - 0.1) , 'R')
plt.plot(O[0], O[1], 'o')
plt.text(O[0] * (1 + 0.1), O[1] * (1 - 0.1) , 'O')

#mention angle POR = 100 degrees on plot
plt.text(Q[0] * (1 + 0.2), Q[1] * (1 - 0.2) , r'$\angle POR = 100^{\circ}$')

plt.savefig('/home/lokesh/EE2802/EE2802-Machine_learning/9.10.5.3/figs/circle.png')