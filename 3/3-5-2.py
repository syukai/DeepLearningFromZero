#オーバーフロー対策を講じたソフトマックス関数
import numpy as np

a = np.array([1010,1000,990])
print("np.exp(a) / np.sum(np.exp(a))")
print(np.exp(a) / np.sum(np.exp(a)))

c = np.max(a)
print("c = np.max(a)")
print(c)

print("a-c")
print(a-c)

print("np.exp(a-c) / np.sum(np.exp(a-c))")
print(np.exp(a-c) / np.sum(np.exp(a-c)))

