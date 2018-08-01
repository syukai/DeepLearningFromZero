# 4-3-3 偏微分
import numpy as np
#import matplotlib.pylab as plt
from numerical_diff import numerical_diff

def function_2(x):
    return x[0]**2 + x[1]**2
    # return np.sum(x**2) でも可... こっちのほうがnumpyぽい

def function_tmp_1(x):
#    return lambda t:function_2([x, 2.0])
    return x**2 + 4.0**2


print(numerical_diff(function_tmp_1, 3.0))
print(numerical_diff(function_tmp_1, 4.0))
