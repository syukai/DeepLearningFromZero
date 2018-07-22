import numpy as np
import matplotlib.pyplot as plt

# 基本型用
# def step_function(x):
#     if x > 0:
#         return 1
#     else:
#         return 0

# numpyに対応
def step_function(x):
    y = x>0
    return y.astype(np.int)

x= np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1) # y軸の範囲を指定
plt.show()

