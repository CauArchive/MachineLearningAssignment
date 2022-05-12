import numpy as np

# p = 3
# x = [1, 2, 3, 4, 5, 6, 7, 8]
# n = len(x)
# A = np.zeros([n, p])
# for i in range(p):
#     A[:, i] = x
# print(A)
# B = np.array([1, 2, 3])
# C = B * A
# print(C)

theta = np.array([-0.02809329,  0.36071584, -0.4335038])
# point = np.array([1., -20., -20.])
point = np.array([[1., -20., -20.],
                  [1., -20., -20.]])
print(theta @ point.T)
