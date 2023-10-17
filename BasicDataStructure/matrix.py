import numpy as np

a = np.array([[1, 2, 3, 4], [4, 55, 1, 2], [8, 3, 20, 19], [11, 2, 22, 21]])
m = np.reshape(a, (4, 4))

print(m)

# accessing element
print("accessing element")
print(a[1])
print("\t", a[2][0])

# Adiing element
print("Adiing element")
m = np.append(m, [[1, 15, 13, 11]], 0)
print(m)

# deleting element
print("deleting element")
m = np.delete(m, [4], 0)
print(m)
