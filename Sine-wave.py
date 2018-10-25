import matplotlib.pyplot as plt
import numpy as np

# compute th x and y co-ordinates for points on a sine curve

x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)
plt.plot(x, y, 'Xr')
plt.show()
