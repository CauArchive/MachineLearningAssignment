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


def something(x):
    print(x.shape)


theta = np.array([[2,  1, 3]]).T
something(theta)
# point = np.array([[1., -20., -20.],
#                   [1., -20., -20.]])
# print(theta * point)
