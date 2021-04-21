import numpy as np 
import matplotlib.pyplot as plt
import math as mt

k = 100000

range_data = 16
hist = np.zeros(range_data, dtype=int)
hit = 0
def p(x):
	return np.exp(-x)

hit = 0
for i in range(0, k):
	x = 8*np.random.random_sample()
	y = np.random.random_sample()
	if y < p(x):
		hit = hit + 1
		count = 0
		for m in np.arange(0.5, 8.5, 0.5):
			if m-0.5 <= x < m:
				hist[count] = hist[count] + 1
			count = count + 1

# u, inv = np.unique(hist, return_inverse=True)
# counts = np.bincount(inv)
u = np.arange(0.5, 8.5, 0.5)
plt.bar(u, hist/0.5/hit, width=0.5, align="edge")
plt.ylabel('p(x)')
plt.xlabel('x')
plt.show()
