import numpy as np

a = np.arange(15).reshape(3, 5)
print(a)

array = ([[ 0, 1, 2, 3, 4],
        [ 5, 6, 7, 8, 9],
        [10, 11, 12, 13, 14]])
print(a.shape)

print(a.ndim)
print(a.dtype.name)
print("item size\t", a.itemsize)
print("size\t", a.size)
print(type(a))

b = np.array([6,7,8])
print(b)
print(type(b))