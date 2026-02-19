# ------------------------------------ Numpy ------------------------------------------

# import numpy as np
# a = 34
# print(a)
# print(type(a))

# import numpy as np
# a = 34
# arr_1 = np.array(a)
# print(arr_1)
# print(type(arr_1))

# import numpy as np
# a = 34,23,45
# arr_1 = np.array(a)
# print(arr_1)
# print(arr_1.ndim)
# print(arr_1.shape)

# import numpy as np
# a = [[2,3,4,5,6,8]]
# arr_1 = np.array(a)
# print(arr_1)
# print(arr_1.ndim)
# print(arr_1.shape)
# print(type(arr_1))

# ---> function for creating 1 D array
# --> arrange = np.array(start,end,step)
# import numpy as np
# a = np.array(10)
# print(a)
# print(type(a))
# print(a.shape)
# print(a.ndim)

# ------> linspace = np.linspace(start,end,number_of_sample)
# import numpy as np
# a = np.linspace(1,5,5)
# print(a)
# print(type(a))
# print(a.shape)
# print(a.ndim)

# ------> Zeros = np.zero((2,))
# import numpy as np
# a = np.zeros((2,))
# print(a)
# print(type(a))
# print(a.shape)
# print(a.ndim)

# ------> ones = np.ones((2,))
# import numpy as np
# a = np.ones((2,2))
# print(a)
# print(a.shape)
# print(a.ndim)
# print(type(a))

# ------> random.randint = np.random.randint(start,end,sample)
# import numpy as np
# a = np.random.randint(1,5,10)
# print(a)
# print(type(a))
# print(a.shape)
# print(a.ndim)

# -- accessing element / exteracting the values
# (1).accessing a single value through indexing
# import numpy as np
# a = np.arange(10,51,10)
# print(a)
# print(type(a))
# print(a.shape)
# print(a.ndim)
# print(a[1])
# print(a[-1])

# (2). accessing a multiple values based on slicing
# import numpy as np
# a = np.arange(10,50,10)
# print(a)
# print(a[1:50:2])

# (3).accessing a multiple values based on indexing
# import numpy as np
# a = np.arange(10,51,10)
# print(a)
# print(a[[0,1,2,3]])

# (4). accessing a multiple value based on condition
# import numpy as np
# a = np.array([34,46,68,77])
# print(a[a % 2 == 0])
# print(a)

# -------> modify the values in numpy
# ----> add a single value in a array
# --> np.append(array,value)

# import numpy as np
# a = np.array([23,34,45,56])
# a1 = np.append(a,100)
# print(a1)
# print(type(a))

# -----> add a multiple values in a array
# import numpy as np
# a = np.array([34,45,56,67])
# a2 = np.append(a,[34,45,56,57])
# print(a2)

# -----> replacing a single value in a 1D array
# import numpy as np
# a = np.array([34,34,45,47,78])
# a[0] = 100
# print(a)

# ------> replacing  multiple values with a single values in array
# import numpy as np
# a = np.array([12,23,34,45,56])
# print(a)
# a[[1,2]] = 12
# print(a)

# ------> replacing a multiple values with multiple values in a array
# import numpy as np
# a = np.array([12,23,34,45,56])
# print(a)
# a[[1,2,3]] = [70,80,90]
# print(a)

# ------> delete a single value in a array
# import numpy as np
# a = np.array([23,34,45,45])
# print(a)
# a2 = np.delete(a,1)
# print(a2)

# ------> delete multiple value in a array
# ---> np.delete(array,[multiple_index])
# import numpy as np
# a = np.array([45,56,67,89])
# print(a)
# a1 = np.delete(a,[0,1])
# print(a1)

# -----> copy array
# import numpy as np
# a = np.array([12,34,45,67])
# b = a.copy()
# b[0] = 100
# print(a)
# print(b)
# print(a)

# ------> sorting an array
# import numpy as np
# a = np.array([4,5,6,9,3])
# b = np.sort(a)
# print(b)

# -------------------> operation of array
# import numpy as np
# a = np.array([1,2,3])
# b = a + 1
# print(b)

# import numpy as np
# a = np.array([3,4,5])
# b = a * 2
# print(b)

# -----------------> camparision operations 
# import numpy as np
# a = np.array([1,2,3,4,5])
# b = np.array([5,6,7,8,9])
# print(a == b)

# import numpy as np
# a = np.array([5,6,7,8])
# b = np.array([1,2,3,4])
# print(a>=b)

# import numpy as np
# a = np.array([12,23,34,45])
# b = np.array([11,22,33,44])
# print(np.array_equal(a,b))

# ---------> mathematical function 
# import numpy as np
# a = np.array([1,2,3,4])
# print(np.exp(a))

# import numpy as np
# a = np.array([1,2,3,4,5])
# print(np.log(a))

# ---------------------------------------- 2 D Array ------------------------------------------
