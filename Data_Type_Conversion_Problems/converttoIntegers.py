import numpy as np;

array = np.array([1.7,2.3,3.9] , dtype='int')
print(array)

# dtype truncates the decimal values

rounded_arr =  np.round(array).astype(int)
print(rounded_arr)
