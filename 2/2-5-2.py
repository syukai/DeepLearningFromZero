# numpyを使ったパーセプトロンの実装
import numpy as np

def perceptron(x1, x2, w1, w2, b):
    x=np.array([x1, x2])
    w=np.array([w1, w2])
    tmp = np.sum(w*x)+b
    if tmp<=0:
        return 0
    else:
        return 1

def AND(x1, x2):
    return perceptron(x1, x2, 0.5, 0.5, -0.7)


def NAND(x1, x2):
    return perceptron(x1, x2, -0.5, -0.5, 0.7)

def OR(x1, x2):
    return perceptron(x1, x2, 0.5, 0.5, -0.2)

def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

print("XOR(0,0)")
print(XOR(0,0))
print("XOR(1,0)")
print(XOR(1,0))
print("XOR(0,1)")
print(XOR(0,1))
print("XOR(1,1)")
print(XOR(1,1))
