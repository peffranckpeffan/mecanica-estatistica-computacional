import numpy as np
import matplotlib.pyplot as plt
import pprint as pp
import collections as coll

T = 2
tempo = 10000
L = 20
N = L*L

S1 = np.ones((L, L), dtype=int)
S = 2*np.random.randint(2, size=(L,L))-1
mag = np.zeros(tempo, dtype=float)
mag1 = np.zeros(tempo, dtype=float)
del_E = 0
for t in np.arange(0,tempo):
	
	for i in np.arange(0, L):
		#i = np.random.randint(0,N)
		#print(i)
		x = np.random.randint(0,L)
		y = np.random.randint(0,L)
		
		up = y - 1 if y != 0 else L-1
		left = x - 1 if x != 0 else L-1
		right = x + 1 if x != L-1 else 0
		down = y + 1 if y != L-1 else 0

		del_E = 2*S[y][x]*(S[down][x] + S[up][x] + S[y][left] + S[y][right])
		del_E1 = 2*S1[y][x]*(S1[down][x] + S1[up][x] + S1[y][left] + S1[y][right])
		if del_E <= 0 or np.random.random_sample() < np.exp(-del_E/T):
			S[y][x] = -1*S[y][x]
		if del_E1 <= 0 or np.random.random_sample() < np.exp(-del_E1/T):
			S1[y][x] = -1*S1[y][x]

	mag[t] = np.sum(S)/N
	mag1[t] = np.sum(S1)/N

x = np.arange(0,tempo)
print(mag)
y = mag
y1 = mag1
m, = plt.plot(x,y, label="aleatorio")
m1, = plt.plot(x,y1, label="um")
plt.legend([m, m1], ['+-1', '1'])
plt.title('L=20 T=2')
plt.ylabel('m')
plt.xlabel('t(MCS)')
plt.show()