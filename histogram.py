import matplotlib.pyplot as plt
import numpy as np

a = np.array([22, 56, 7, 8, 9, 0, 33, 44, 5, 6, 88, 8, 8, 66])
np.histogram(a, bins=[0, 20, 40, 60, 80, 100])
hist, bins = np.histogram(a, bins=[0, 20, 40, 60, 80, 100])

print(hist)
print(bins)
plt.hist(a, bins=[0, 20, 40, 60, 80, 100])
plt.title("histogram")
plt.show()
