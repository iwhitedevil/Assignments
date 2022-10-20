import numpy as np
a = np.arange(0,5)
b = np.arange(5,10)
c = np.arange(10,15)

d = np.array([a,b,c],dtype=float)
print('Floating Array:',d)

print('First method',d.astype(np.int64))
d = np.array([a,b,c],dtype=int)
print('Integer Array 2nd method:',d)
