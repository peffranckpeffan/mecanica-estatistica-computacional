import numpy as np
import matplotlib.pyplot as plt

T0 = 4
dT = 0.04
L = 5
N = L*L

t_max = 10000

S = np.ones((L, L), dtype=int)
#S = 2*np.random.randint(2, size=(L,L))-1

e = np.zeros(int(T0/dT), dtype=float)
m = np.zeros(int(T0/dT), dtype=float)

S_r = np.ones((L, L), dtype=int)
#S = 2*np.random.randint(2, size=(L,L))-1

e_r = np.zeros(int(T0/dT), dtype=float)
mag_med = np.zeros(int(T0/dT), dtype=float)

def atualiza1MCS(S, T):
	for i in np.arange(0, L):

		x = np.random.randint(0,L)
		y = np.random.randint(0,L)

		up = y - 1 if y != 0 else L-1
		left = x - 1 if x != 0 else L-1
		right = x + 1 if x != L-1 else 0
		down = y + 1 if y != L-1 else 0

		del_E = S[y][x]*(S[down][x] + S[up][x] + S[y][left] + S[y][right])

		if del_E <= 0 or np.random.random_sample() < np.exp(-2*del_E/T):
			S[y][x] = -1*S[y][x]
	return S

def magnetizacao(S):
	return np.sum(S)/N

def energia(S):
	energ = 0
	for i in np.arange(0, L):
		for j in np.arange(0,L):

			up = i - 1 if i != 0 else L-1
			left = j - 1 if j != 0 else L-1
			right = j + 1 if j != L-1 else 0
			down = i + 1 if i != L-1 else 0

			energ -= S[i][j]*(S[down][j] + S[up][j] + S[i][left] + S[i][right])
	return energ/N

T = 0
T_r = T0
count = 0
for tt in np.arange(0.04, T0, dT):
	for t in range(0, t_max):
		atualiza1MCS(S,tt)
		mag_med[count] += abs(magnetizacao(S))/t_max 
	
	count += 1


x = np.arange(0, T0, dT)
pm, = plt.plot(x, mag_med, 'o', label="magnetizacao")
plt.title('L=5')
plt.xlabel('T')
plt.ylabel('<m>')
plt.xlim(0,3.9)
plt.show()

#np.savetxt('test.out', np.c_[x_r,m_r])