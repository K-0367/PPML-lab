#wap to data types and structure in numpy
import numpy as np
arr=np.array([1,2,3],dtype='int32')
print('DATA TYPE:',arr.dtype)
arr=arr.astype("float64")
print("UPDATED type:",arr.dtype)
