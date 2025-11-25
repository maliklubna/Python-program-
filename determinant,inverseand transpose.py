import numpy as np
arr = np.random.randint(10, size=(3, 3))
print("Original array is:\n", arr)
determinant = np.linalg.det(arr)
print(f"Determinant = {determinant}")
inverse = np.linalg.inv(arr)
print("Inverse =\n", inverse)
transpose = arr.T
print("Transpose:\n", transpose)