import numpy as np

n1 = np.array([[np.sqrt(3)],[1]])
n2 = np.array([[1],[np.sqrt(3)]])

N = n1.T@n2
D = np.linalg.norm(n1)*np.linalg.norm(n2)
A = np.degrees(np.arccos(N/D))
print(A, "degrees")