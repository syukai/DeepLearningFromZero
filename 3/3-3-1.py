import numpy as np

A = np.array([1,2,3,4])

print(A)


print("np.ndim(A)")
print(np.ndim(A))   # 1

print("A.shape")
print(A.shape) # (4,) ... tuple

print("A.shape[0]")
print(A.shape[0])  # 4

print("")

B = np.array([[1,2],[3,4],[5,6]])
print("B")
print(B)

print("np.ndim(B)")
print(np.ndim(B))

print("B.shape")
print(B.shape)
