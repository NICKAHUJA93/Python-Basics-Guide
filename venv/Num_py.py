import numpy as np
# creating alias for numpy
run = np.array([[1,2,3],[4,5,6]])
print(run)
# shape property is used to calculate the dimension of array
print(run.shape)
# item size is used to calculate the size of individual element of array
print((run.itemsize))
# ndim is used to calcuate the dimension of array
print((run.ndim))
# type is used to check dimension of array
print((type(run)))
# division of array
run2 = np.array([[1,2,3],[4,5,6]])
print(run2)
run3 =np.divide(run,run2)
print(run3)
# Reverse the array : Slicing of an array
run4 =([1,2,3,4,5,6,7,8,9,10])
print(run4[::-1])
#loop accessing in python
#python does not allow circular loop
print(run4[0:3:-1])
#index starting ,ending and stepsize
print(run4[0:8:2])
#Arange function creates a new array
run5 =np.arange(20)
print(run5)
# change the shape of array where number of element remain constant
print(run.shape)
run.shape=(6,1)
print(run)
run.shape=(1,6)
print(run)
#ravel function is used to create a horizontal array
#run6 = run4.ravel()
#print(run6)
print("creating a new array for 9*9")
run6 =np.array([[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]])
print(run6.shape)
print(run6)
#slicing of 9*9 matrix
print("Matrix 1")
print(run6[0:3:1,0:3:1])
print("Matrix 2")
print(run6[3:6:1,3:6:1])
print("Matrix 3")
print(run6[6:9:1,6:9:1])
print("Matrix 4")
print(run6[3:6:1,0:3:1])
print("Matrix 5")
print(run6[3:6:1,3:6:1])
print("Matrix 6")
print(run6[3:6:1,6:9:1])
print("Matrix 7")
print(run6[6:9:1,0:3:1])
print("Matrix 8")
print(run6[6:9:1,3:6:1])
print("Matrix 9")
print(run6[6:9:1,6:9:1])