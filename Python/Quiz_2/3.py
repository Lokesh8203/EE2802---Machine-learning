#Find the coord of foot of perpendicular from the point (-1, 3) on the line 3x - 4y = 16

import numpy as np

omat = np.array([[0,1],[-1,0]])

#Foot of the Perpendicular
def perp_foot(n,cn,P):
  m = omat@n
  N=np.block([[n],[m]])
  p = np.zeros(2)
  p[0] = cn
  p[1] = m@P
  #Intersection
  x_0=np.linalg.inv(N)@p
  return x_0

n = np.array([3,-4])
cn = 16
P = np.array([-1,3])

x_0 = perp_foot(n,cn,P)
print(x_0)