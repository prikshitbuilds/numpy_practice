# Indexing means accessing individual elements of an array by their position.
# In a 1D array (vector) → you use a single index.
# In a 2D array (matrix) → you use row and column indices.


# Slicing means selecting a range of elements (a sub-array) instead of a single element.

# Uses the start:stop:step notation.

# start → index to begin from (inclusive)

# stop → index to end at (exclusive)

# step → how much to skip each time (default = 1)


# 1D ARRAY INDEXING

import numpy as np;
arr= np.array([10,20,30,40])

print(arr[0])
print(arr[2])
print(arr[-1])

#2D ARRAY INDEXING
arr_2d = np.array([[1,2,3],[4,5,6]])

print(arr_2d[0][2]) # 3
print(arr_2d[-1][-1]) # 6
print(arr_2d[-1][-2]) #5





###### SLICING

# for vector
slicing_arr= np.array([1,2,3,4,5])

print(slicing_arr[1:4]) # 2 3 4
print(slicing_arr[:3]) # 1 2 3
print(slicing_arr[::2]) # 1 3 5

print(slicing_arr[::-1]) # reverse
print(slicing_arr[-1:]) # last leem
print(slicing_arr[:-1:])


# 2d array slicing

matrx= np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])


print(matrx[0:2,1:3])

print(matrx[:,0]) # 1 4 7
print(matrx[0,:]) # 1 2 3

# mixing indexing & slicing

mix_matrix = np.array([[10,20,30],
                       [40,50,60],
                       [70,80,90]])

print(mix_matrix[0,1:])

print(mix_matrix[1:,2])



# masking

masking =np.array([10,20,30,40,50])

mask = masking > 30
print(masking[mask])

# 40 50


