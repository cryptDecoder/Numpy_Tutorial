import matplotlib.pyplot as plt
import numpy as np

x = [5, 7, 8, 9, 0]
y = [12, 34, 5, 76, 7]

x2 = [3, 5, 6]
y2 = [5, 6, 77]

plt.bar(x, y, align='center')
plt.bar(x2, y2, color='g', align='center')

plt.title('Bar Graph')
plt.ylabel('y Axix')
plt.xlabel('x axis')

plt.show()
