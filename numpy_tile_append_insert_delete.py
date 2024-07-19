import numpy as np

a = np.array([10,20,60,80])
b = np.array([[10,20],[60,80]])

print(np.tile(a,(3,1)))
print(np.append(a,90))
print(np.append(b,[90,100]))
print()
print(np.insert(a,1,50))

print(np.delete(a,1))
print()