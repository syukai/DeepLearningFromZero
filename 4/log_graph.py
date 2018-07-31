import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,1, 0.01)
y = np.log2(x)
y2 = np.log10(x)
y3 = np.log(x)

plt.plot(x, y, label="2")
plt.title("log 2")
plt.ylim(-5, 0.2)
plt.show()

plt.plot(x, y2, label="10")
plt.title("log 10")
plt.ylim(-5, 0.2)
plt.show()

plt.plot(x, y3, label="e")
plt.title("log e")
plt.ylim(-5, 0.2)
plt.show()
