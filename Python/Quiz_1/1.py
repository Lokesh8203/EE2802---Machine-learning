#Find the relation between x and y if (x,y), (1,2), and (7,0) are collinear

import numpy as np
from sympy import symbols, Matrix, simplify
from sympy.plotting import plot
x, y = symbols("x, y")

A = np.array([x,y])
B = np.array([1,2])
C = np.array([7,0])

eq = simplify(Matrix([B-A, C-A]).det())
print("The relation between x and y is", eq, "= 0")