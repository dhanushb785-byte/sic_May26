'''import numpy as np
array1 = np.zeros(3)
print(array1)
array2=np.zeros((3,3),dtype=int)
print(array2)
print('middle element')
print(array2[1][1])
array3 = np.full((3,3),7,dtype = float)
print(array3)
print(type(array3))
'''
'''
import numpy as np
# arange()

array1 = np.arange(10)
array2 = np.arange(10, 20)
array3 = np.arange(10, 30, 3)

print(type(array1))
print(array1)
print(array2)
print(array3)'''

import numpy as np

vector = np.arange(5)
print('Vector shape:', vector.shape)

matrix = np.ones([3, 2])
print('Matrix:', matrix)
print('Matrix shape:', matrix.shape)

tensor = np.zeros([2, 3, 3])
print('Tensor:', tensor)
print("Tensor shape:", tensor.shape)
