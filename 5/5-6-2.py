import numpy as np

x_dot_W = np.array([[0, 0, 0], [10, 10, 10]])
B = np.array([1, 2, 3])

print("X_dot_W" + str(x_dot_W))

print("X_dot_W + B =" + str(x_dot_W + B))

dY = np.array([[1, 2, 3], [4, 5, 6]])
print("dY = " + str(dY))

dB = np.sum(dY, axis=0)
print("dB = " + str(dB))
