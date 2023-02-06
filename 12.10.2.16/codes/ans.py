#Find the position vector of the mid point of the vector joining the points P(2, 3, 4) and Q(4, 1, –2).

import numpy as np
import matplotlib.pyplot as plt

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

p = np.array([2.0,3.0,4.0])
q = np.array([4.0,1.0,-2.0])

#mid point of the vector joining the points P and Q
m = (p+q)/2
print("Mid point of the vector joining the points P and Q is", m)

x_pq = line_gen(p,q)
plt.plot(x_pq[0,:],x_pq[1,:],label='$PQ$')
plt.plot(p[0],p[1],'k.')
plt.text(p[0],p[1], "P")
plt.plot(q[0],q[1],'k.')
plt.text(q[0],q[1], "Q")
plt.plot(m[0],m[1],'k.')
plt.text(m[0],m[1], "M")
plt.grid()
plt.tight_layout()
plt.axis('equal')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.savefig('/home/lokesh/EE2802/EE2802-Machine_learning/12.10.2.16/figs/line.png')