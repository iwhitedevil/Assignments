import numpy as np
a = np.arange(0,5)
b = np.arange(5,10)
c = np.arange(10,15)
d = np.array([a,b,c])
print('First Array is :',d , end='\n')

e = np.copy(d)
print('Second Array is :',e,end='\n')
f = np.add(d,e)
print('Addition Of First & Second Array :',f)
