import pandas as pd
import numpy as np
# where pd represent as alias for pandas
# In pandas we consider dictionary in which keys are converted into column and values get converted into rows for dataframe
# creating and printing a data frame
data = pd.DataFrame({'Country':['India','Japan','Australia','China','Russia'],'Economy Rank':[1,2,3,4,5]})
print(data)
# quick analysis of data is done by describe function
print(data.describe())
# To know the information about the data frame we use info function
print(data.info())
#Lets create a new data frame
data1 = pd.DataFrame({'group':['A','B','C','D','E','A','C','D'],'ounce':[10,20,10,20,40,10,20,30]})
print(data1)
# create a data frame in ascending order
# implace is False it won't change original data frame
print(data1.sort_values(by=['ounce'],ascending=True,inplace=False))
print("making value of inplace as true")
print(data1.sort_values(by=['ounce'],ascending=True,inplace=True))
#Sorting a data frame by multiple columns
print(data1.sort_values(by=['ounce','group'],ascending=[True,True],inplace=False))
# Duplicate rows are basically noise ,before training any model we need to remove a noise
data2=pd.DataFrame({'k1':['one']*3+['Two']*4,'k2':[1,2,3,5,4,5,6]})
print(data2)
print(data2.sort_values(by='k2'))
# Now remove dulpicate row
print(data2.duplicated())

############## Series #################
#Series is used to create an array
data3=pd.Series([1,2,3,4,5,6,7,8,9])
print(data3)
data3.replace([1,2,3],[np.nan,np.nan,np.nan],inplace=True)
print(data3)
#How to rename rows and column
# arrange function will create array
#reshape will with 5*5 matrix
#index will give row
#Column will give name of column
data4 =  pd.DataFrame(np.arange(25).reshape(5,5),index = ['A','B','C','D','E'],columns = ['one','two','three','four','fifth'])
print(data4)
# rename specific index and column in a data frame
data5 = data4.rename(index = {'A':'a','B':'b'},columns = {'one' :'ONE','two':'TWO' })
print(data5)
# upercase and lower case in data frame
data6 = data5.rename(index = str.upper())
print(data6)

