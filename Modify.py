import numpy as np

a = np.arange(0, 60, 5)
a = a.reshape(3, 4)

print("\n original Array :")
print(a)

print("\n Sorted array  in c- style order :")
for x in np.nditer(a, order='C'):
    print(x, )

print("\n Sorted in F-style order:")
for x in np.nditer(a, order='F'):
    print(x, )

print("modified array :")
a[...] = 2 * a
print(a)
