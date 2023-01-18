#If a,b,c are unit vectors with a + b + c = 0, then find a.b + b.c + c.a

import numpy as np

a = np.array([np.cos(2*np.pi/3), np.sin(2*np.pi/3)])
b = np.array([np.cos(4*np.pi/3), np.sin(4*np.pi/3)])
c = np.array([np.cos(0), np.sin(0)])

print(a)
print(b)
print(c)

print(a@b + b@c + c@a)