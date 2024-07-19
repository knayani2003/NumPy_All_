import numpy as np

ar = np.array([10,20,30,40])

print(np.sum(ar))
print(np.min(ar))
print(np.max(ar))
print(np.size(ar))
print(np.mean(ar))
print(np.cumsum(ar))
print(np.cumprod(ar))

price = np.array([10,20,30])
qty = np.array([5,2,3])

print(price)
print(qty)
print()

c = np.cumprod([price,qty], axis=0)
print(c[1].sum())