import numpy as np

int_ones = np.ones((2,2), dtype=np.int8)
print(int_ones)

print(int_ones.dtype)

float_ones = np.ones((2, 2), dtype=np.float16)
print(float_ones)

print(float_ones.dtype)

int_ones[1, 1] = -1
print(int_ones)