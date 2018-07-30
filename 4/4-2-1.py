# 2乗和誤差
import numpy as np
def mean_squared_error(y, t):
    return 0.5 * np.sum((y-t)**2)

# 「2」を正解とする
t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]

# 2の確率が最も高い場合
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
print("mean_squared_error(np.array(y), np.array(t))")
print(mean_squared_error(np.array(y), np.array(t)))

# 7の確率が最も高い場合
y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
print("mean_squared_error(np.array(y), np.array(t))")
print(mean_squared_error(np.array(y), np.array(t)))

# 2の確率が最も高い場合(さらに確率を上げてみた)
y = [0.05, 0.05, 0.7, 0.0, 0.05, 0.1, 0.0, 0.05, 0.0, 0.0]
print("mean_squared_error(np.array(y), np.array(t))")
print(mean_squared_error(np.array(y), np.array(t)))

