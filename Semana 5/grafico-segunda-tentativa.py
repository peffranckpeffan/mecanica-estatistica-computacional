import numpy as np 
import matplotlib.pyplot as plt
import math as mt
import pprint as pp

N = 20
E = 60
E_m = E/N
tempo = 10000

osciladores = np.zeros(N, dtype=int)
oscilador0 = np.zeros(tempo, dtype=int)
oscilador0_1 = np.zeros(tempo, dtype=int)
hist = np.zeros(E, dtype=int)

fazer_hist = False

osciladores[0] = E
count = 0
for t in range(0, tempo):
	n = int(np.floor(np.random.random_sample()*N))
	m = int(np.floor(np.random.random_sample()*N))
	
	if osciladores[n] > 0:
		osciladores[n] = osciladores[n] - 1
		osciladores[m] = osciladores[m] + 1

	oscilador0[t] = osciladores[0]

	if oscilador0[t] == E_m:
		fazer_hist = True

	if fazer_hist == True:
		hist[osciladores[0]] = hist[osciladores[0]] + 1
		oscilador0_1[t] = osciladores[0]


print(oscilador0)
x = np.arange(0, tempo)
y = oscilador0
plt.plot(x,y)
#plt.axhline(3, color="red")
plt.ylabel('V[0]')
plt.xlabel('t')
plt.show()

# transiente = int(input())
# #transient = 12000

# s = np.zeros(tempo-transiente, dtype=int)
# count = 0
# for i in range(transiente, tempo):
#    s[count] =  oscilador0[i]
#    count = count + 1

u, inv = np.unique(oscilador0_1, return_inverse=True)
counts = np.bincount(inv)
plt.bar(u, counts, width=0.5, align="center")
plt.yscale('log')
plt.ylabel('P0(k)')
plt.xlabel('k')
plt.show()

# u = np.arange(0, E, 1)
# plt.yscale('log')
# plt.bar(u, hist, width=0.5, align="center")
# plt.ylabel('p0(k)')
# plt.xlabel('k')
# plt.show()