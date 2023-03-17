# -*- coding: utf-8 -*-
"""panda_tutorial

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1f0jSh28DRja051b48rqpreEwh5OXxA66
"""

import numpy as np
print('Library imported.')

print(np.__version__)

x=np.array([1,2,3,4,5])
x

type(x)

#2d array
y=np.array(
  
        [1,22,3]
)
y
q=np.array([2,3,4])

y.ndim

np.concatenate((x,y))

# to concatenate along rows
x=np.array([[1,22,3],[2,3,5]])
y=np.array([[4,5,6],[4,1,2]])

np.concatenate((x,y),axis=1)

np.concatenate((x,y),axis=0)

#Using the stack function

a=np.stack((x,y))

a.ndim



#3D
three_dim=np.array(
    [
        
    [3,4,5],
    [2,3,4],
    [1,2,3]
    ]  
)
three_dim

x=np.ones((2,2),dtype='int')
x

type(x[0,0])

x=np.array(
    [1,2,3]
)
y=np.array([3,4,5])
#to add arrays
np.add(x,y)

np.subtract(x,y)

np.multiply(x,y)

np.sqrt(x)

np.dot(x,y)

#we have broadcasting

x=np.array([2,4,6])
x

import pandas as pd
print('Libraries imported')

x=[1,2,3,4]

y=pd.Series(x, index=['Mon','Tues','Wed','Thurs'])
y

data={
    'name':'Kenneth',
    'age':23,
    'class':'master'
}
type(data)
pd_series=pd.Series(data)
pd_series

#Creating data frames
data=[1,2,3]
z=pd.DataFrame(data)
z

#s

real=[[1,2,3],[3,4,5]]
s=pd.DataFrame(real)
s.loc[2]=[100,200,300]
s#loc,grabs a particular row and to make change

type(y)

dataset=pd.read_csv('Iris.csv')
dataset

#check the head,checks first 5 rows
dataset.head()

dataset.head(20)

dataset.tail()

#to check the shape
dataset.shape

dataset.info()



"""## Data Preprocessing"""

# duplicates,empty,null

data=pd.read_csv('Iris_modified.csv')

data

data.info()

#how to use dropvalue
x=data.dropna()#will drop all null values
x

#save previous in variable or

#to fill null places with numbers
Data=pd.read_csv('Iris_modified.csv')
y=Data.fillna(200)
y

#to fill for specific columns
Data.PetalWidthCm



Data['PetalWidthCm']=Data['PetalWidthCm'].fillna(500)

Data

mean_PL=Data.PetalLengthCm.mean()

mean_PL

mean_SL=Data.SepalLengthCm.mean()
mean_SW=Data.SepalWidthCm.mean()
mean_PL=Data.PetalLengthCm.mean()
mean_PW=Data.PetalWidthCm.mean()

print(f'This is sepal length:{mean_SL}')
print(f'This is sepal width:{mean_SW}')
print(f'This is petal length :{mean_PL}')
print(f'This is petal width: {mean_PW}')

Data['SepalLengthCm']=Data['SepalLengthCm'].fillna(mean_SL)
Data['SepalWidthCm']=Data['SepalWidthCm'].fillna(mean_SW)
Data['PetalLengthCm']=Data['PetalLengthCm'].fillna(mean_PL)
Data['PetalWidthCm']=Data['PetalWidthCm'].fillna(mean_PW)

Data

Data.info()

#you can use mode,median,mean..use diff dataset for all of them then implement,and fllna h all

#how to remove duplicates
Data=Data.drop_duplicates()

Data.duplicated()

Data

"""## Data analysis"""

#Filtering

Data.filter(items=['SepalWidthCm'])

Data.filter(like='Petal')#Any column name that looks'like' it is printed out

#Sorting
Data.sort_values('SepalLengthCm')#helps us to find outliers and see the range well

#we can sort in ascending or descending order for ascending set to true
Data.sort_values('SepalWidthCm',ascending=False)

#Correlation. You can make some deductions from here such as how the different parameters 

Data.corr()

