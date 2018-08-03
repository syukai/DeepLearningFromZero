import sys, os
sys.path.append(os.pardir)
import numpy as np
from simpleNet import simpleNet
from common.gradient import numerical_gradient

def f(W):
    return net.loss(x, t)

net = simpleNet()
print("net.W")
print(net.W)

x = np.array([0.6, 0.9])
p = net.predict(x)
print("net.predict([0.6, 0.9])")
print(p)

np.argmax(p)

#正解ラベルを使って損失を計算
t = np.array([0, 0, 1])
print("net.loss(x, t)")
print(net.loss(x, t))

dW = numerical_gradient(f, net.W)
print("numerical_gradient(f, net.W)")
print(dW)

print(numerical_gradient((lambda w: net.loss(x, t)), net.W))
