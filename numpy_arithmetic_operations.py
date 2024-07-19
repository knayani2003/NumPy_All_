import numpy as np

arr1 = np.array([10,20,30,40])
arr2 = np.array([50,60,70,80])

print(arr1+arr2)
print(np.add(arr1,arr2))

print(arr1-arr2)
print(np.subtract(arr1,arr2))

print(arr1*arr2)
print(np.multiply(arr1,arr2))

print(arr1/arr2)
print(np.divide(arr1,arr2))

arr1 = np.array([2,3,4,5])
arr2 = np.array([2])

print(np.power(arr1,arr2))

arr3 = np.power(arr1,arr2)

print(np.sqrt(arr3))