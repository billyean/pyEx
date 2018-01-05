import numpy as np

mvalues = [0, 1, 5, 6, 80]
print("mvalues =", mvalues)

# array will create a matrix array
M = np.array(mvalues)
print("M = ", M)

print(M * 39.3701) #conversion to inches

# arange is provide a start, end and step also with conversion. Be careful conversion is not happening on the result
# instead it happens to step
x1 = np.arange(20, 104.75, 3.6)
x2 = np.arange(20, 104.75, 3.6, np.int_)
print(x1)
print(x2)

# linspace is distributes points between start and end with number.
xl = np.linspace(20, 104.75, 5, endpoint = False)
print(xl)
