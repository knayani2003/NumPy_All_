import numpy as np
import statistics as st

bf = np.array([200,300,150,130,200,280,170,188])

print(np.mean(bf))
print(np.median(bf))
print(st.mode(bf))
print(np.std(bf))
print(np.var(bf))

tc = [30,50,10,30,50,40]
d = [100,120,70,100,120,112]

print (np.corrcoef([tc,d]))