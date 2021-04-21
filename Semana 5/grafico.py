import numpy as np 
import matplotlib.pyplot as plt
import math as mt
import pprint as pp

N = 30000
E = 100

states = np.zeros(E, dtype=int)
state_0 = np.zeros(N, dtype=int)
hist = np.zeros(E, dtype=int)

states[0] = E
count = 0
for state in range(0, N):
	n = int(np.floor(np.random.random_sample()*E))
	m = int(np.floor(np.random.random_sample()*E))
	
	if states[n] > 0:
		states[n] = states[n] - 1
		states[m] = states[m] + 1

	state_0[state] = states[0]

	if state > 12000:
		hist[states[0]] = hist[states[0]] + 1


print(hist)
# x = np.arange(0, N)
# y = state_0
# plt.plot(x,y)
# #plt.axhline(3, color="red")
# plt.ylabel('V[0]')
# plt.xlabel('t')
# plt.show()

# transient = int(input())
#transient = 12000

# s = np.zeros(N-transient, dtype=int)
# count = 0
# for i in range(transient, N):
#    s[count] =  state_0[i]
#    count = count + 1

# u, inv = np.unique(s, return_inverse=True)
# counts = np.bincount(inv)
# print(u)
# plt.bar(u, counts/N, width=1, align="edge")
# plt.ylabel('frequencia/M')
# plt.xlabel('k')
# plt.show()

u = np.arange(0, 100, 1)
plt.bar(u, hist/N, width=1, align="edge")
plt.ylabel('p(k)')
plt.xlabel('k')
plt.show()