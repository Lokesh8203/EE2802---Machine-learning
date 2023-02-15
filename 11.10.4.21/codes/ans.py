#Find equation of the line which is equidistant from parallel lines 9x + 6y – 7 = 0 and 3x + 2y + 6 = 0

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from math import *

def norm(n):
    return sqrt(n[0]*n[0] + n[1]*n[1])

n1 = np.array([1,2/3])
n2 = np.array([1,2/3])
c1 = 7/9
c2 = -2

x1 = sp.Symbol('x1')
x2 = sp.Symbol('x2')
x = np.array([x1, x2])

#two cases for absolute
#Case 1
equation_1 = (n1@x - c1)/norm(n1) - (n2@x - c2)/norm(n2)
print(equation_1, "= 0")
print("This is not possible\n")

#Case 2
equation_2 = (n1@x - c1)/norm(n1) + (n2@x - c2)/norm(n2)
print(equation_2, "= 0")

#fig code

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
x = np.linspace(-5,5,100)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
plt.plot(x, (7/6)-(3/2)*x, '-r', label='9x+6y-7=0')
plt.plot(x, (-3/2)*(x) - 3,'-g', label='3x+2y+6=0')
plt.plot(x, (-3/2)*x - (11/12),'-b', label='18x+11y+12=0')
plt.legend(loc='upper right')
plt.savefig('/home/lokesh/EE2802/EE2802-Machine_learning/11.10.4.21/figs/line.png')