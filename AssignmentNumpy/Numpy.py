# Import NumPy as np
import numpy as np
# Create an array of 10 zeros
arr1 = np.zeros(10)
print(arr1)
# Create an array of 10 ones
arr2 = np.ones(10)
print(arr2)
# Create an array of 10 fives
arr3 = np.ones(10) * 5
print(arr3)
# Create an array of the integers from 10 to 50
arr4 = np.arange(10, 51)
print(arr4)
# Create an array of all the even integers from 10 to 50
arr5 = np.arange(10, 51, 2)
print(arr5)
# Create a 3x3 matrix with values ranging from 0 to 8
arr6 = np.arange(9).reshape(3, 3)
print(arr6)
# Create a 3x3 identity matrix
arr7 = np.eye(3)
print(arr7)
# Use NumPy to generate a random number between 0 and 1
rand_number = np.random.rand(1)
print(rand_number)
# Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution
rand_number2 = np.random.rand(25)
print(rand_number2)

arr8 = np.arange(1, 101).reshape(10, 10)
print(arr8)


arr9 = np.linspace(0, 1, 20)
print(arr9)

arr10 = np.arange(1, 26).reshape(5, 5)
print(arr10)
print("#" * 50)
print(arr10[2:, 1:])
print("#" * 50)
print(arr10[3, 4])
print("#" * 50)
print(arr10[:3, 1:2])
print("#" * 50)
print(arr10[4:])
print("#" * 50)
print(arr10[3:5:])
print("#" * 50)
print(arr10.sum())
