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
# import numpy as np
# a = np.array([[1,2,3,4],[6,7,8,9]])
# print(a)
# print(type(a))
# print(a.shape)
# print(a.ndim)

#----> zero = np.zeros() # it is give values in decimal so we can convret into the int
# import numpy as np
# a = np.zeros((2,3))
# print(a)
# print(a.shape)
# print(a.ndim)
# print(type(a))

# import numpy as np
# a = np.zeros((2,3),dtype=int)
# print(a)
# print(type(a))
# print(a.ndim)
# print(a.shape)

# ------> ones = np.ones() it is also give value in the form of decimal
# import numpy as np
# a = np.ones((2,3),dtype=int)
# print(a)
# print(type(a))
# print(a.shape)
# print(a.ndim)

# ------> identity metrix = np.eye()
# import numpy as np
# a = np.eye(3,3)
# print(a)
# print(type(a))
# print(a.shape)
# print(a.ndim)

# -----> diagonal metrix = np.diag()
# import numpy as np
# a = np.diag([1,2,3,4])
# print(a)
# print(type(a))
# print(a.ndim)
# print(a.shape)


# ---------------> indexing of 2D array
# all the columns in row start by 0 by default
# import numpy as np
# a = np.array([[1,2,3,4],[6,7,8,9],[9,8,7,6]])
# print(a)
# print(type(a))
# print(a.shape)
# print(a.ndim)
# print(a[0])
# print(a[1:3])

# ----> assigning the values in 2D array
# import numpy as np
# a = np.array([[1,2,3,4],[5,6,7,8],[12,23,34,45]])
# print(a)
# a[1] = [23,34,45,47]
# print(a)
# a[0,3] = 500
# print(a)

#-------------------> flattening
# ----> Flattening in NumPy is the process of converting a multi-dimensional array into a one-dimensional array.
# import numpy as np
# a = np.array([[2,3,4,5],[6,7,8,9]])
# print(a)
# print(a.shape)
# print(a.ndim)
# print(type(a))

# b = a.ravel()
# print(b)
# print(b.shape)
# print(b.ndim)
# print(type(b))

# -----> reshape() is used to change the shape of a NumPy array without changing its data.
# import numpy as np
# a = np.array([1,2,3,4])
# print(a)
# print(a.shape)
# print(a.ndim)
# print(type(a))

# a1 = a.reshape(2,2)
# print(a1)
# print(type(a1))
# print(a1.shape)
# print(a1.ndim)


#----> a.T returns the transpose of array a by swapping rows and columns.
# import numpy as np
# a = np.array([[1,2,3,4],[5,6,7,8]])
# print(a)
# print(a.shape)
# print(a.ndim)
# print(type(a))

# b = a.T
# print(b)
# print(b.shape)
# print(b.ndim)
# print(type(b))

# -----> sort array
# sorting along an axis : axis = 1---row and axis = 0 ---columns
# import numpy as np
# a = np.array([[1,2,1],[4,5,3],[7,8,2]])
# b = np.sort(a,axis=1)
# print(b.shape)
# print(b.ndim)
# print(b)
# print(a)

# import numpy as np
# a = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(a)
# print(a.shape)
# print(a.ndim)
# b = np.sort(a,axis=0)
# print(b)
# print(b.shape)
# print(b.ndim)

# ---> adding two array
# import numpy as np
# a = np.array([[1,2,3],[4,5,6],[7,8,9]])
# b = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(a+b)

# import numpy as np
# a = np.array([[1,2,3],[4,5,6]])
# b = np.array([[1,2,3],[4,5,6]])
# print(a + b)

# ----> mutmul = np.matmul() works by multiplying rows of the first matrix with columns of the second matrix and summing the results.
# import numpy as np
# a = np.array([[1,2],[5,6]])
# b = np.array([[1,2],[5,6]])
# c = np.matmul(a,b)
# print(c)


# concatinate = np.concatenate() is used to join two or more NumPy arrays into a single array along a specified axis.

# import numpy as np
# a = np.array([[1,2,3],[5,6,7],[7,8,9]])
# b = np.array([[4,5,6],[6,7,8],[2,8,5]])
# c = np.concatenate((a,b),axis=0)
# print(c)

# import numpy as np
# a = np.array([[1,2],[5,6]])
# b = np.array([[4,5],[6,7]])
# c = np.concatenate((a,b),axis=1)
# print(np.concatenate((a,b),axis=0))
# print(c)


# =========================================  Pandas ==============================================

# Pandas is a Python library used for data manipulation and analysis using Series and DataFrame
# Main Data Structures in Pandas
# Series → 1D data (single column)
# DataFrame → 2D data (rows + columns, like Excel)

# ----------------> Series = Single column of data with index
# import pandas as pd
# s = pd.Series([1,2,3,4,5,6])
# print(s)

# import pandas as pd
# s = pd.Series(["a","b","c","d","e"])
# print(s)

# import pandas as pd
# import numpy as np
# s = pd.Series(np.random.randint(5),index = ['a','b','c','d','e'])
# print(s)


# import numpy as np
# import pandas as pd
# dictonary = {'a':1,'b':2,'c':3,'d':4}
# s = pd.Series(dictonary)
# print(s)

# import pandas as pd
# import numpy as np
# dict = {'a':1,'b':2,'c':3,'d':4,'e':5}
# s1 = pd.Series(dict)
# print(s1)
# array = [1,2,3,4,5]
# s2 = pd.Series(array)
# print(s2)

# import pandas as pd
# import numpy as np
# dict = {'a':1,'b':2,'c':3,'d':4,'e':5}
# s1 = pd.Series(dict)
# print(s1)
# print(s1['a'])
# print(s1[['a','b']])


# import numpy as np
# import pandas as pd
# array = pd.Series([1,2,3,4,5])
# print(array)
# print(array[[0,1,2]])


# import pandas as pd
# import numpy as np

# dict = {'a':1,'b':2,'c':3,'d':4,'e':5}
# s1 = pd.Series(dict)
# print(s1)

# array = [1,2,3,4,5]
# s2 = pd.Series(array)
# print(s2)
# print(s1[2:])
# print(s2[2:])
# print(s1[:2])
# print(s2[:2])

# assing a vlaue

# import pandas as pd
# import numpy as np
# dict = {'a':1,'b':2,'c':3,'d':4,'e':5}
# s1 = pd.Series(dict)
# print(s1)

# array = [1,2,3,4,5]
# s2 = pd.Series(array)
# print(s2)

# s1['a'] = 100
# s2[1] = 200
# print(s1)
# print(s2)

# -->get values by index
# import pandas as pd
# import numpy as np
# dict = {'a':1,'b':2,'c':3,'d':4}
# s1 = pd.Series(dict)
# print(s1.get('b'))
# s1 = s1 + 3
# print(s1)

#------------------------------> Data Frame
# A DataFrame is a two-dimensional labeled data structure in pandas used to store and manipulate data in tabular form.

# import pandas as pd
# import numpy as np
# s = pd.DataFrame(columns=['a','b','c','d','e'])
# print(s)
# print(s.ndim)
# print(s.shape)
# print(type(s))

# import numpy as np
# import pandas as pd

# s = pd.DataFrame(columns=['a','b','c','d','e'],index=range(1,6))
# print(s)

# dataframe passing a dict
# import pandas as pd
# import numpy as np
# dict = {'A':[1,2,3,4,5],
#          'B':[2,3,4,5,6]}
# print(pd.DataFrame(dict))

# creating a dataframe passing a numpy with datatime index

# import pandas as pd
# dates = pd.date_range("2025-01-01", periods=5)
# df = pd.DataFrame({"Sales": [10, 20, 30, 40, 50]}, index=dates)
# print(df)

# import pandas as pd
# import numpy as np
# dict = {'a':1,'b':2,'c':3,'d':4,'e':5}
# print(pd.DataFrame([dict]))

# import pandas as pd
# import numpy as np

# dict = pd.DataFrame({'A':np.random.randn(10),
#                      'B':np.random.randn(10),
#                      'C':np.random.randn(10)})[]
# print(dict)
# # if we won't first three rows
# print(dict.head(3))
# import pandas as pd
# import numpy as np
# df = pd.DataFrame({'A':np.random.randn(10),
#                    'B':np.random.randn(10),
#                    'C':np.random.randn(10)})
# print(df.tail(3))


# get the data frame index
# import pandas as pd
# import numpy as np
# df = pd.DataFrame({'A':np.random.randn(10),
#                    'B':np.random.randn(10),
#                    'C':np.random.randn(10)})
# print(df)
# print(df.index)

# get the data frame columns
# import pandas as pd
# import numpy as np
# df=pd.DataFrame({'A':np.random.randn(10),
#                  'B':np.random.randn(10),
#                  'C':np.random.randn(10)})
# print(df.columns)

# get the data frame values
# import pandas as pd
# import numpy as np
# df = pd.DataFrame({'A':np.random.randn(10),
#                    'B':np.random.randn(10),
#                    'C':np.random.randn(10)})
# print(df.values)

# ------> import data frame csv file

# import pandas as pd
# import numpy as np
# df = pd.read_csv(r"C:\Users\imrat\OneDrive\Desktop\data_science_all_uses_items\test.csv",usecols=[0,1],nrows=10)
# print(df)

# import pandas as pd
# import numpy as np
# df = pd.read_csv(r"C:\Users\imrat\OneDrive\Desktop\data_science_all_uses_items\test.csv",usecols=[0,1])
# print(df.head())
# print(df.shape)

# selecting a single columns
# import pandas as pd
# import numpy as np
# df = pd.read_csv(r"C:\Users\imrat\OneDrive\Desktop\data_science_all_uses_items\test.csv")
# print(df.head(5))
# print(df.shape)
# close = df['x']
# print(close.head(5))

# selecting multiple columns 
# import pandas as pd
# import numpy as np
# df = pd.read_csv(r"C:\Users\imrat\OneDrive\Desktop\data_science_all_uses_items\test.csv")
# closeval = df[['x','y']]
# print(closeval.head())

#selecting rows via 
# ----> we can select a set of rows by index
# import pandas as pd
# import numpy as np
# df = pd.read_csv(r"C:\Users\imrat\OneDrive\Desktop\data_science_all_uses_items\test.csv")
# print(df[10:15])

# ----> we can select a set of rows and columns
# import pandas as pd
# import numpy as np
# df = pd.read_csv(r"C:\Users\imrat\OneDrive\Desktop\data_science_all_uses_items\test.csv")
# print(df[10:15][['x','y']])

#----> selecting via .loc[] (by lable)
# Uses row labels (index names) and column names
# Use .loc when you know column names or conditions

# import pandas as pd
# import numpy as np
# df = pd.read_csv(r"C:\Users\imrat\OneDrive\Desktop\data_science_all_uses_items\test.csv")
# print(df.loc[10:15,['x','y']])

# selecting via .iloc[] (by position)
# Uses row numbers (0,1,2...) and column positions
# Use .iloc when you want row/column by position
# import pandas as pd
# import numpy as np
# df = pd.read_csv(r"C:\Users\imrat\OneDrive\Desktop\data_science_all_uses_items\test.csv")
# print(df.iloc[10:15])

# import pandas as pd
# import numpy as np
# df = pd.read_csv(r"C:\Users\imrat\OneDrive\Desktop\data_science_all_uses_items\test.csv")
# print(df.iloc[10:15,[0,1]])

# import pandas as pd
# import numpy as np
# df = pd.read_csv(r"C:\Users\imrat\OneDrive\Desktop\data_science_all_uses_items\test.csv")
# print(df)
# print(df[df.x>100])
# print(df[(df['x']>50) | (df['x']<100)])

# ------------- manipulation a data frame 
# --> transpose using 
# the pandas data frame treanspose function T allows us to transpose function the row as columns and logically the columns as row

# import pandas as pd
# import numpy as np
# df = pd.read_csv(r"C:\Users\imrat\OneDrive\Desktop\data_science_all_uses_items\test.csv")
# df2 = df[10:15][['x','y']]
# print(df2.T)

# -- the sort_index method
#df.sort_index() is used to sort a pandas DataFrame by its index (row labels or column labels).
# import pandas as pd
# import numpy as np
# df = pd.read_csv(r"C:\Users\imrat\OneDrive\Desktop\data_science_all_uses_items\test.csv")
# print(df.sort_index())

# -- the sort_values() method 
# --->sort_values() is used to sort a DataFrame based on column values, not index.
# import pandas as pd
# import numpy as np
# df = pd.read_csv(r"C:\Users\imrat\OneDrive\Desktop\data_science_all_uses_items\test.csv")
# print(df.sort_values(by='y'))

# import pandas as pd
# import numpy as np
# df = pd.read_csv(r"C:\Users\imrat\OneDrive\Desktop\data_science_all_uses_items\test.csv")
# print(df)
# print(df.sort_values(['x','y']))

# the reindex() function 
# --> we wont to reindex row and columns
# import pandas as pd
# import numpy as np
# df = pd.DataFrame(np.random.randn(5),index=['a','b','c','d','e'])
# print(df)

# print(df.reindex(['a','b','c','e','d']))

# import pandas as pd
# import numpy as np
# df = pd.DataFrame(np.random.randn(5))
# print(df)
# print(df.reindex([4,3,2,1,0]))

# -----> adding new columns 
# import pandas as pd
# import numpy as np
# df = pd.DataFrame(np.random.randn(5))
# print(df)
# df['new'] = 21
# print(df)


# ------> delete an existing columns 
# import pandas as pd
# import numpy as np
# df = pd.DataFrame(np.random.randn(5,4))
# print(df)
# del df[0]
# print(df)

# - the .at() (by label)
# -->In pandas, .at() is used to access or set a single value in a DataFrame very fast
# import pandas as pd
# import numpy as np
# df = pd.DataFrame(np.random.randn(5,4))
# print(df)
# print(df.at[0,0])

# import pandas as pd
# import numpy as np
# df = pd.DataFrame(np.random.randn(5,4),index=['a','b','c','d','e'],columns=['A','B','C','D'])
# print(df)
# print(df.at['a','A'])
# df.at['a','A'] = 0
# print(df)

# ----> the .iat()
# ---->In pandas, .iat() is used to get or set ONE single value from a DataFrame using integer position (row & column numbers).
# import pandas as pd
# import numpy as np
# df = pd.DataFrame(np.random.randn(5,4))
# print(df)
# print(df.iat[0,0])

# statistical exploratary data analysis (EDA)

# import pandas as pd
# import numpy as np
# df = pd.DataFrame(np.random.randn(5,4),index=['a','b','c','d','e'],columns=['A','B','C','D'])
# print(df)
# print(df.info())

# ----> the describe() function 
# import pandas as pd
# import numpy as np
# df = pd.DataFrame(np.random.randn(5,4),index=['a','b','c','d','e'],columns=['A','B','C','D'])
# print(df)
# print(df.describe())

# ----> value.count()
# import pandas as pd
# import numpy as np
# df = pd.DataFrame(np.random.randn(5,4),index=['a','b','c','d','e'],columns=['A','B','C','D'])
# print(df)
# print(df['A'].value_counts())

# ----> the mean() function 
# import pandas as pd
# import numpy as np
# df = pd.DataFrame(np.random.randn(5,4),index=['a','b','c','d','e'],columns=['A','B','C','D'])
# print(df.mean(axis=0)) # by columns
# import pandas as pd
# import numpy as np
# df = pd.DataFrame(np.random.randn(5,4),index=['a','b','c','d','e'],columns=['A','B','C','D'])
# print(df.mean(axis=1)) # by row

# ----> the std() function 
# ----> .std() returns how much the values spread out from the mean (average).
# import pandas as pd
# import numpy as np
# df = pd.DataFrame(np.random.randn(5,4),index=['a','b','c','d','e'],columns=['A','B','C','D'])
# print(df['A'].std()) # by columns 

# import pandas as pd
# import numpy as np
# df = pd.DataFrame(np.random.randn(5,4),index=['a','b','c','d','e'],columns=['A','B','C','D'])
# print(df['A'].std(axis=0))

# ----> filtring pandas data frame
#Filtering in a Pandas DataFrame is the process of selecting specific rows and/or columns from a DataFrame based on given conditions or criteria.
# import pandas as pd
# import numpy as np
# df = pd.DataFrame(np.random.randn(5,4),index=['a','b','c','d','e'],columns=['A','B','C','D'])
# print(df)
# df_f1 = df[df['A'] > 0]
# print(df_f1)

# ----> we also create multiple condition
# import pandas as pd
# import numpy as np
# df = pd.DataFrame(np.random.randn(5,4),index=['a','b','c','d','e'],columns=['A','B','C','D'])
# df_filter=df[(df['A'] > 0)]
# print(df_filter)

# import pandas as pd
# import numpy as np
# df = pd.DataFrame(np.random.randn(5,4),index=['a','b','c','d','e'],columns=['A','B','C','D'])
# print(df)
# df_filter = df[(df['A'] > 0) & (df['B'] > 0)]
# print(df_filter)

# ----> iterating pandas DataFrame
# iterrows() is used to iterate over DataFrame rows, returning index and row data as a Series.
# import pandas as pd
# import numpy as np
# df = pd.DataFrame(np.random.randn(5,4),index=['a','b','c','d','e'],columns=['A','B','C','D'])
# print(df)
# for item in df.iterrows():
#     print(item)

# ----> merge append and concat pandas data frame
# To combine related data stored in different DataFrames
# To match rows using a common key (like id, roll_no, etc.)
#The merge() function in Pandas is used to combine two DataFrames by matching rows based on one or more common columns (keys).
# import pandas as pd
# df1 = pd.DataFrame({
#     'id': [1, 2, 3],
#     'name': ['Aman', 'Ravi', 'Neha']
# })
# df2 = pd.DataFrame({
#     'id': [2, 3, 4],
#     'marks': [85, 90, 88]
# })
# result = pd.merge(df1, df2, on='id')
# print(result)

# import pandas as pd
# import numpy as np
# df1 = pd.DataFrame(np.random.randn(5,4),index=['a','b','c','d','e'],columns=['A','B','C','D'])
# print(df1)
# print("DataFrame : 1")
# df2 = pd.DataFrame(np.random.randn(5,4),index=['a','b','c','d','e'],columns=['A','B','C','D'])
# print(df2)
# print("dataFrame : 2")
# df3 = pd.merge(df1,df2)
# print(df3)
# print("dataFrame : 3")

# concat function
#concat allows us to merge two data frmae by rows and columns 
# it by default rows
# import pandas as pd
# import numpy as np
# df1 = pd.DataFrame(np.random.randn(5,4),index=['a','b','c','d','e'],columns=['A','B','C','D'])
# print(df1)

# df2 = pd.DataFrame(np.random.randn(5,4),index=['a','b','c','d','e'],columns=['A','B','C','D'])
# print(df2)

# df3 = pd.concat([df1,df2])
# print(df3)

#---> for columns
# import pandas as pd
# import numpy as np
# df1 = pd.DataFrame(np.random.randn(5,4),index=['a','b','c','d','e'],columns=['A','B','C','D'])
# print(df1)
# df2 = pd.DataFrame(np.random.randn(5,4),index=['a','b','c','d','e'],columns=['A','B','C','D'])
# print(df2)

# df3 = pd.concat([df1,df2],axis=1)
# print(df3)












      










