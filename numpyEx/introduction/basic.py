import numpy as np

# Single value operation
x = np.random.random()
print("Random number : ", x)
x_square_root = np.sqrt(x)
print("Square root of x : ", x_square_root)
print("x^sqrt(x) : ", np.power(x, x_square_root))

# Matrix creation and operation
mx = np.random.random(3)
print("Random matrix : ", mx)
mx = np.append(mx, np.random.random(2))
print("After appending matrix : ", mx)
print("Sin matrix : ", np.sin(mx))