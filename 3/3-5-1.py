# ソフトマックス関数
import numpy as np

a = np.array([0.3, 2.9, 4.0])

# ネイピア数のn乗
# numpy配列を入力にするのでmath.expではなくnumpyのexpを使う
exp_a = np.exp(a)
print("exp_a")
print(exp_a)    # [  1.34985881  18.17414537  54.59815003]

# Σの計算
sum_exp_a = np.sum(exp_a)
print("sum_exp_a = np.sum(exp_a)")
print(sum_exp_a)    # 74.1221542102

y = exp_a / sum_exp_a
print("y = exp_a / sum_exp_a")
print(y)            # [ 0.01821127  0.24519181  0.73659691]
