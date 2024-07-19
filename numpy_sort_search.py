import numpy as np

ar1 = np.array([15,2,6,12,7])
ar2 = np.array([[15,2,5],[6,12,7]])

print(np.sort(ar1))
# print(np.sort(ar2))

# s = np.where(ar1 == 6)
# print(s)

ss = np.searchsorted(ar1,6)
print(ss)