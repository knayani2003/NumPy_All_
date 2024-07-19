import numpy as np

ar1 = np.array([10,20])
ar2 = np.array([5,3])

print(np.concatenate([ar1,ar2]))

arr1 = np.array([[10,20],[30,40]])
arr2 = np.array([[4,3],[5,6]])

print(np.hstack([arr1,arr2]))
print(np.vstack([arr1,arr2]))

a = np.array([10,20,30,40,50,60])
print(np.array_split(a,3))

b =  np.array_split(a,3)
print(b[1])