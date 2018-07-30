import numpy as np
#import math

def cross_entropy_error(y, t):
    delta = 1e-7    #浮動小数点表現の0.0000001
    return -np.sum(t * np.log(y + delta))

t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
print("cross_entropy_error(np.array(y), np.array(t))")
print(cross_entropy_error(np.array(y), np.array(t)))

t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
print("cross_entropy_error(np.array(y), np.array(t))")
print(cross_entropy_error(np.array(y), np.array(t)))

print(- np.log(0.1)) #これとほぼ同じのはず
