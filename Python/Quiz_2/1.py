#Find the equation of line parallel to the line 3x - 4y = 2 and passing through the point (-2, 3)
import numpy as np
from matplotlib import pyplot as plt


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

#Orthogonal matrix
omat = np.array([[0,1],[-1,0]]) 

n = np.array([3,-4])
A = np.array([-2,3])

p = omat@n
B = A + n

x_AB = line_gen(A,B)
plt.plot(x_AB[0],x_AB[1])
plt.plot(A[0],A[1],'k.')
plt.text(A[0],A[1], "A")
plt.grid()
plt.savefig("/home/lokesh/EE2802/EE2802-Machine_learning/Python/Quiz_2/figs/1.png")
