import numpy as np
A = np.array([[1,2,3],[4,5,6]])
print(A)

B=np.array([[1,2],[5,6],[7,8]])
print(B)

print("np.dot(A, B)")
print(np.dot(A, B))

C=np.array([1,2],[3,4])
print("C")
print(C)

print("np.dot(A, C)")
print(np.dot(A, C)) #error!
