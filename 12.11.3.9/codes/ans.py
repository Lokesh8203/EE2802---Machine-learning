#Find the equation of the plane through the intersection of the planes 3x–y + 2z–4 = 0 and x + y + z–2 = 0 and the point (2,2,1)

import numpy as np
import sympy as sp

# Define the planes
p1 = np.array([3, -1, 2, -4])
p2 = np.array([1, 1, 1, -2])

lambda_ = sp.symbols('lambda')
print('Equation of the plane through the intersection of the planes 3x–y + 2z–4 = 0 and x + y + z–2 = 0 and the point (2,2,1) is:', p1 + lambda_*(p2))

equation = (p1 + lambda_*(p2))[0:3]@np.array([2, 2, 1]) + (p1 + lambda_*(p2))[3]

lambda_ = sp.solve(equation, lambda_)[0]

normal = (p1 + lambda_*(p2))[0:3]
print('The equation of plane is {}x + {}y + {}z + {} = 0'.format(normal[0], normal[1], normal[2], (p1 + lambda_*(p2))[3]))