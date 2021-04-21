import numpy as np 
import matplotlib.pyplot as plt

count = 0
M = 1000
x = np.zeros(M)
y = np.zeros(M)
hit = 0

for m in range(1,M):
	rand_num = np.random.random_sample()
	if rand_num < 0.5:
		hit  = hit + 1
	y[m] = hit/m
	x[m] = m


plt.plot(x, y)
plt.axhline(0.5, color="gray")
plt.ylabel('<k>')
plt.xlabel('m')
plt.show()