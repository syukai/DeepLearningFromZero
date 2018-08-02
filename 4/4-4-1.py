import numpy as np
from gradient_descent import gradient_descent

def function_2(x):
    return x[0]**2 + x[1]**2

init_x = np.array([-3.0, 4.0])
x1 = init_x
x2 = np.array([-3.0, 4.0])
x3 = np.array([-3.0, 4.0])
print("gradient_descent(function_2, init_x=init_x, lr=0.1, step_num=100)")
print(gradient_descent(function_2, init_x=init_x, lr=0.1, step_num=100))

print("gradient_descent(function_2, init_x=init_x, lr=10.0, step_num=100)")
print(gradient_descent(function_2, init_x=init_x, lr=10.0, step_num=100))

print("gradient_descent(function_2, init_x=init_x, lr=1e-10, step_num=100)")
print(gradient_descent(function_2, init_x=init_x, lr=1e-10, step_num=100))
