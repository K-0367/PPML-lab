#create an Numpy array with elements[10,20,30,40].
import numpy as np
arr = np.array([10, 20, 30, 40])
print(arr)

#create a 2D array and display its shape and dimension
import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print(arr)
print("Shape:", arr.shape)
print("Dimension:", arr.ndim)

#create arrays using zeros(),ones() and empty()
import numpy as np

a = np.zeros((2, 3))
b = np.ones((2, 3))
c = np.empty((2, 3))

print("Zeros:\n", a)
print("Ones:\n", b)
print("Empty:\n", c)

#convert a 1D array into 2D array.
import numpy as np

arr1 = np.array([10, 20, 30, 40])
arr2 = arr1.reshape(2, 2)

print(arr2)

#Access specific elements and slices in an array.
#performm addition ,substraction and multiplication of arrays.
#find the mean medianand standard deviation.