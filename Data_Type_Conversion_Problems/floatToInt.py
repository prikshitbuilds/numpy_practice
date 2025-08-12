import numpy as np;

float_arr=np.array([1.5,1.4,1.1,1.2,1.9,1.0], dtype=float)
int16_arr = float_arr.astype(np.int16)
print(int16_arr)