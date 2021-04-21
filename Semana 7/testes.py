import numpy as np 
L = 10
N = L*L
x=2*np.random.randint(2, size=(N,N))-1
print(np.sum(x))