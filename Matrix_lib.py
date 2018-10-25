'''
	Numpy package contains a matrix library numpy.matlib this 
	module has function that returns matrices instead of ndarray objects

'''
import numpy as np
import numpy.matlib

# matlib.empty
print(np.matlib.empty((2, 3)))

# ---------------------------------

# np.matlib.zeros()
print(np.matlib.zeros((2, 2)))

# -----------------------------------

# np.matlib.ones()
print(np.matlib.ones((2, 3)))

# ----------------------------------------

'''numpy.matlib.eye()
This function returns a matrix with 1 along the diagonal elements and the zeros elsewhere. The function takes the following parameters.'''

print(np.matlib.eye(n=3, M=4, k=0, dtype=float))

# ---------------------------------------------------

'''numpy.matlib.identity()
The numpy.matlib.identity() function returns the Identity matrix of the given size. An identity matrix is a square matrix with all diagonal elements as 1'''

print(np.matlib.identity(5, dtype=float))

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''numpy.matlib.rand()
The numpy.matlib.rand() function returns a matrix of the given size filled with random values.'''

print(np.matlib.rand(3, 3))

# -------------------------------------------------------------------------------------------------------------


'''NumPy package contains numpy.linalg module that provides all the functionality required for linear algebra. Some of the important functions in this module are described in the following table.

Sr.No.	Function & Description
1	dot
Dot product of the two arrays

2	vdot
Dot product of the two vectors

3	inner
Inner product of the two arrays

4	matmul
Matrix product of the two arrays

5	determinant
Computes the determinant of the array

6	solve
Solves the linear matrix equation

7	inv
Finds the multiplicative inverse of the matrix'''
