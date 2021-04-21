import numpy as np 
import matplotlib.pyplot as plt

M = 1001
N = 6
x = np.zeros(M)
y = np.zeros(M)
x1 = np.zeros(M)
y1 = np.zeros(M)
aver = 0
aver2 = 0

for m in range(1,M):
	hit = 0
	for i in range(1,N):
		rand_num = np.random.random_sample()
		if rand_num < 0.5:
			hit = hit + 1

	aver = aver + hit
	aver2= aver2 + hit*hit
	y[m] = aver/m
	x[m] = m
	y1[m] = aver2/m - np.power(aver/m,2)
	x1[m] = m


plt.plot(x, y)
plt.plot( x1, y1)
plt.axhline(2.5, color="gray")
plt.axhline(1.25, color="red")
plt.ylabel('<k>')
plt.xlabel('m')
plt.show()