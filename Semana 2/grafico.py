import numpy as np 
import matplotlib.pyplot as plt

M = 10000
N = 5
hist = np.zeros(M, dtype=int)

for m in range(0,M):
	hit = 0
	for i in range(0,N):
		rand_num = np.random.random_sample()
		if rand_num < 0.5:
			hit = hit + 1

	hist[m] = hit

hist = hist
# with open("tst", "w") as file:
# 	for i in range(0,M):
# 		file.write(str(hist[i]) + '\n')
# print(hist.size)
# plt.hist(hist, align="left")

# plt.show()
# print(hist)
# histogram = np.histogram(hist)
# print(histogram)

# plt.hist(hist)

# plt.xlim(-1,6)
# plt.show()

u, inv = np.unique(hist, return_inverse=True)
counts = np.bincount(inv)
print(hist)
print(hist.size)
print(u)
print(inv)
print(counts)
#plt.bar(u, counts/M, width=0.5)
#plt.ylabel('frequencia/M')
#plt.xlabel('k')
#plt.show()