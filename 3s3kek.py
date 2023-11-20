import numpy as np
from scipy.linalg import solve

A = np.array([[3,2,[2,-1]])
b = np.array([12,1]).reshape((2,1))

x = solve(A,b)
print(x)
