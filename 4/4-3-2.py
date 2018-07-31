import numpy as np
import matplotlib.pylab as plt
from numerical_diff import numerical_diff

def function_1(x):
    """
    サンプル関数
    """
    return 0.01*x**2 + 0.1*x

def tangent_line(f, x_):
    d = numerical_diff(f, x_)
    print("d")
    print(d)
    y = f(x_) - d*x_      # xの位置で元の数式に接するようにx時点の値を算出
    print("y")
    print(y)
    return lambda t: d*t + y

x = np.arange(0.0, 20.0, 0.1)
y = function_1(x)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x, y)

print("pythonによる数値微分")
print("numerical_diff(function_1, 5)")
print(numerical_diff(function_1, 5))
print("numerical_diff(function_1, 10)")
print(numerical_diff(function_1, 10))

y2 = tangent_line(function_1, 5)(x)
y3 = tangent_line(function_1, 10)(x)
plt.plot(x, y2)
plt.plot(x, y3)
plt.show()
