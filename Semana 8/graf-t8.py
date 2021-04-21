import numpy as np
import matplotlib.pyplot as plt

T0 = 4
dT = 0.0004
L = 5
N = L*L

S = np.ones((L, L), dtype=int)
#S = 2*np.random.randint(2, size=(L,L))-1

e = np.zeros(int(T0/dT), dtype=float)
m = np.zeros(int(T0/dT), dtype=float)

S_r = np.ones((L, L), dtype=int)
#S = 2*np.random.randint(2, size=(L,L))-1

e_r = np.zeros(int(T0/dT), dtype=float)
m_r = np.zeros(int(T0/dT), dtype=float)

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
for t in np.arange(0, T0, dT):
	T = T + dT
	
	
	#Aquecimento
	S = atualiza1MCS(S, T)
	e[count] = energia(S)
	m[count] = magnetizacao(S)

	#Resfriamento
	S_r = atualiza1MCS(S_r, T_r)
	e_r[count] = energia(S_r)
	m_r[count] = magnetizacao(S_r)
	#print(T_r)
	T_r = T_r - dT
	count += 1




x = np.arange(0, T0, dT)
x_r = np.arange(T0, 0 , -dT)
pe, = plt.plot(x, e, label="energia")
pm, = plt.plot(x, m, label="magnetizacao")
pe_r, = plt.plot(x_r[:-10], e_r[:-10], label="energia_r")
pm_r, = plt.plot(x_r[:-10], m_r[:-10], label="magnetizacao_r")
plt.axhline(0, color="red")
plt.legend([pe, pm, pe_r, pm_r], ["e - aquece", "m -aquece", "e - resfria", "m - resfria"])
plt.title('L=20 dT=0.0004')
plt.xlabel('T')
plt.xlim(0,3.9)
plt.show()

#np.savetxt('test.out', np.c_[x_r,m_r])