import numpy as np 
import matplotlib.pyplot as plt

M = 10
N = 1
x = np.zeros(M)
y = np.zeros(M)
aver = 0
aver2 = 0

for m in range(0,M):
	hit = 0
	for i in range(0,N):
		rand_num = np.random.random_sample()
		if rand_num < 0.5:
			hit = hit + 1

	aver = aver + hit
	aver2= aver2 + hit*hit

	k2aver=aver/(m+1)
	kaver2=pow(aver/(m+1),2)

	if m - 1 != 0:
		y[m] = pow( (k2aver - kaver2)/(m-1), 0.5)
	else:
		y[m] = None

	x[m] = m

M = 100
N = 1
x1 = np.zeros(M)
y1 = np.zeros(M)
aver = 0
aver2 = 0
k2aver=0
kaver2=0

for m in range(0,M):
	hit = 0
	for i in range(0,N):
		rand_num = np.random.random_sample()
		if rand_num < 0.5:
			hit = hit + 1

	aver = aver + hit
	aver2= aver2 + hit*hit

	k2aver=aver/(m+1)
	kaver2=pow(aver/(m+1),2)

	if m - 1 != 0:
		y1[m] = pow( (k2aver - kaver2)/(m-1), 0.5)
	else:
		y1[m] = None

	x1[m] = m

M = 1000
N = 1
x2 = np.zeros(M)
y2 = np.zeros(M)
aver = 0
aver2 = 0
k2aver=0
kaver2=0

for m in range(0,M):
	hit = 0
	for i in range(0,N):
		rand_num = np.random.random_sample()
		if rand_num < 0.5:
			hit = hit + 1

	aver = aver + hit
	aver2= aver2 + hit*hit

	k2aver=aver/(m+1)
	kaver2=pow(aver/(m+1),2)

	if m - 1 != 0:
		y2[m] = pow( (k2aver - kaver2)/(m-1), 0.5)
	else:
		y2[m] = None

	x2[m] = m

plt.plot(x, y)
plt.plot(x1, y1)
plt.plot(x2, y2)
plt.ylabel('sigmaN')
plt.xlabel('N')
plt.show()