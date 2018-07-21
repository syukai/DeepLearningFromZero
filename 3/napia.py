import numpy as np
import matplotlib.pyplot as plt

#データ作成
step = 100000
x = np.arange(step*100, step*1000, step)
y = pow(1 + (1/x),x)

#グラフ描画
plt.plot(x, y)
plt.show()