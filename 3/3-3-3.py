import numpy as np

# inputが2つ
X = np.array([1,2])
print("X.shape")
print(X.shape)

# 重み付けされた
W = np.array([[1,3,5], [2,4,6]])
print("W")
print(W)

print("W.shape")
print(W.shape)

Y = np.dot(X, W)
print("Y=np.dot(X,W)")
print(Y)

