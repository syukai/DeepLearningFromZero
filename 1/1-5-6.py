import numpy as np
X=np.array([[51,55],[14,19],[0,4]])

print("X")
print(X)
print("X[0]")
print(X[0])

print("X[0][1]")
print(X[0][1])

print("print each row")
for row in X:
   print(row)

Xd = X.flatten()
print("X.flatten")
print(Xd)

Xdm =Xd[np.array([0, 2, 4])]
print("X.flatten get 0,2,4")
print(Xdm)


print("x>15")
print(X>15)

print("X[X>15]")
print(X[X>15])