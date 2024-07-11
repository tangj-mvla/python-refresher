import numpy as np

#1
a = np.array([1,2,3])
b = np.array([4,5,6])

sum = a+b
diff = a-b
print (f"Sum: {sum}")
print (f"Difference: {diff}")

#2
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

sum = a + b
diff = a - b
print(f"Sum: {sum}")
print(f"Difference: {diff}")

# 3
a = np.array([1,2,3])
b = np.array([4,5,6])
dot = np.dot(a,b)
print(f"Dot Product: {dot}")

# 4
a = np.array([[1,2,3],[4,5,6]])
b = np.array([[7,8,9,10],[11,12,13,14],[15,16,17,18]])
product = np.dot(a,b)
print(f"Produt: {product}")

# 5
a = np.array([1,1,2])
magnitude = np.linalg.norm(a)
print(f"Magnitude: {magnitude}")

# 6
a = np.array([[1,2],[3,4]])
print(f"Transpose: {a.T}")