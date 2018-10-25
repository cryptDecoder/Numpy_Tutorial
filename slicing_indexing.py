import numpy as np

# array to begin with

a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])

print("Our array is :")
print(a)
print("\n")

# this returns array of items in the second column
print("The item in the second column are :")
print(a[..., 1])
print("\n")

# Now we will slice all items from the second row 
print(" The item in the second row are :")
print(a[1, ...])
print("\n")

# Now we will slice all items from column 1 onwords
print("The items column 1 onwards are :")
print(a[..., 1:])

'''
output->

Our array is :
[[1 2 3]
 [3 4 5]
 [4 5 6]]


The item in the second column are :
[2 4 5]


 The item in the second row are :
[3 4 5]


The items column 1 onwards are :
[[2 3]
 [4 5]
 [5 6]]
'''

# Advanced Indexing

print("\n ::: Advanced Indexing :::")
x = np.array([[1, 2], [3, 4], [5, 6]])
y = x[[0, 1, 2], [0, 1, 0]]
print(y)

xx = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print("Our array is :")
print(xx)
print("\n")

row = np.array([[0, 0], [3, 3]])
cols = np.array([[0, 2], [0, 2]])

yx = xx[row, cols]
print("The corner elements of this array are :")
print(yx)

'''
	OUTPUT->
	::: Advanced Indexing :::
[1 4 5]
Our array is :
[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]]


The corner elements of this array are :
[[ 0  2]
 [ 9 11]]
'''

# slicing

zx = xx[1:4, 1:3]
print("\n After slicingm,our array becomes :")
print(zx)
print("\n")

# using advanced index for column 

yc = xx[1:4, [1, 2]]
print(yc)

'''
	output->
		 After slicingm,our array becomes :
[[ 4  5]
 [ 7  8]
 [10 11]]


[[ 4  5]
 [ 7  8]
 [10 11]]
'''

# boolean Array indexing

print("\n the items greater than are 5 are :")
print(xx[xx > 5])

# output -> the items greater than are 5 are :
# [ 6  7  8  9 10 11]
