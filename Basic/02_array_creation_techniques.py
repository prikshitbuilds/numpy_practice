# simple array
import numpy as np;

np.array([1,2,3,4])

# zero array
zero_vector= np.zeros((2,3))
print(zero_vector)

#ones vector
one_vector= np.ones((2,3))
print(one_vector)

# empty vector
empty_vector=np.empty((2,3))
print(empty_vector)

# arrange -> range
range_vector = np.arange(0,10,2)
print(range_vector)

#linespace -> created evenly separted values between two numbers
linespace_vector = np.linspace(0,1,5)
print(linespace_vector)
# [0.   0.25 0.5  0.75 1.  ]

log_space_vector = np.logspace(1,3,4)
print(log_space_vector)
 # [  10.           46.41588834  215.443469   1000.        ]

# eye vector -> diagonal 1s other place 0s
eye_vector = np.eye(3)
print(eye_vector)