'''Matplotlib is a plotting library for Python. 
It is used along with NumPy to provide an environment that is an effective open source alternative for MatLab. 
It can also be used with graphics toolkits like PyQt and wxPython.'''

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 11)
y = x * 2

plt.title("Matplotlib Demo")
plt.xlabel(" X axis Caption")
plt.ylabel("y axis Caption")

plt.plot(x, y, 'ob')
plt.show()
