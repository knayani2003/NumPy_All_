import numpy as np

ar = np.array([10,20,30,40])
ft1 = [True,False,True,False]
ft2 = ar>35

nw1 = ar[ft1]
nw2 = ar[ft2]

print(nw1)
print(nw2)