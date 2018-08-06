import numpy as np
from ReLu import ReLu

x = np.array( [[1.0, -0.5], [-2.0, 3.0]])
print("x=" + str(x))

mask = (x <= 0)
print("x <= 0" + str(mask))

print(x[mask])