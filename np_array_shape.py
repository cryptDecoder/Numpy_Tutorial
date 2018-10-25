import numpy as np

# -----------------------------------------------
# np array shape
arr = np.array([[1, 2, 3, 4], [1, 5, 6, 7]])
print(arr.shape)
# output (2,4) -> it defines that the numner of col and rows in arary
# ----------------------------------------------------------------------------=

# reshape array
x = arr.reshape(4, 2)
print(x)

# -----------------------------------------------------------------------
# np itemsize
print(arr.itemsize)
# output : 4 -> This array attribute returns the length of each elements of array in byts

# ---------------------------------------------------


# np arange
print(np.arange(24))

# printing array in given range

# ------------------------------


# np flags
x = np.array([1, 4, 5, 7, 8])
print(x.flags)

# ---------------------------------

# np.empty -> it creates an uninitalized array of specified shape and dtype.

z = np.empty([3, 2], dtype=int, order='C')
print(z)

# the elements in  array show random values as they are not initialized

# -------------------------------------------------------------------------------------

# np zeros -> returns a new array of specified size, filled with zeros
print(np.zeros(5))
# output -> [0. 0. 0. 0. 0.]

# ---------------------------------------------------------------------------------

# np.ones -> Return a new array of specified size and type, filled with onec
print(np.ones(5))
# output-> [1. 1. 1. 1. 1.]

# -------------------------------------------------------------------------------------

# NumPy - Array from Existing Data

# np.asarray -> This routine is udeful for converting Python sqence in ndArray
a = [1, 2, 3, 5]
xs = np.asarray(x)
print(xs)
# output -> [1 4 5 7 8]
# ---------------------------------------------------------------------------

# np.linspace -> In this function, instead of step size, the number of evenly spaced values between the interval specified.

ln = np.linspace(10, 20, 5)
print(ln)
# output -> [10.  12.5 15.  17.5 20. ]
# --------------------------------------------------

# logspace -> spaced on a log scale.
ls = np.logspace(1.0, 2.0, num=10)
print(ls)
# ------------------------------------------------------

# Numpy - Indexing & slicing

sl = np.arange(10)
ss = slice(2, 7, 2)
print(sl[ss])
# output-> [2 4 6]
