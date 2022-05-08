import numpy as np

p = 3
x = [1, 2, 3, 4, 5, 6, 7, 8]
n = len(x)
A = np.zeros([n, p])
for i in range(p):
    A[:, i] = x
print(A)
B = np.array([1, 2, 3])
C = B * A
print(C)
