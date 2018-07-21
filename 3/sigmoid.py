# can't exec...

import numpy as np
import matplotlib.pyplot as plt
import math as math

# data
step = 1000
x = np.arange(step, step*100, step)
y = math.exp(x)

#glaph
plt.plot(x, y)
plt.show()
