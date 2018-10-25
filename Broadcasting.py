import numpy as np

a = np.array([1, 3, 4, 5, 6])
b = np.array([4, 5, 6, 7, 7])

c = a * b
print(c)

# output -> [ 4 15 24 35 42]


x = np.array([[0.0, 0.0, 0.0], [10.0, 10.0, 10.0], [20.0, 20.0, 20.0], [30.0, 30.0, 30.0]])
y = np.array([1.0, 2.0, 3.0])

print('First array:')
print(x)
print('\n')

print('Second array:')
print(y)
print('\n')

print('First Array + Second Array')
print(x + y)

'''
First array:
[[ 0.  0.  0.]
 [10. 10. 10.]
 [20. 20. 20.]
 [30. 30. 30.]]


Second array:
[1. 2. 3.]


First Array + Second Array
[[ 1.  2.  3.]
 [11. 12. 13.]
 [21. 22. 23.]
 [31. 32. 33.]]
'''
