#Find equation of the line which is equidistant from parallel lines 9x + 6y – 7 = 0 and 3x + 2y + 6 = 0

import numpy as np
import sympy as sp
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
