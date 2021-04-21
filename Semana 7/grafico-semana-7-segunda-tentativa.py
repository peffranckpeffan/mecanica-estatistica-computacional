import numpy as np
import matplotlib.pyplot as plt

T = 2
tempo = 6000
L = 100
N = L*L

S = np.ones((N, N), dtype=int)
S = 2*np.random.randint(2, size=(N,N))-1
mag = np.zeros(tempo, dtype=int)

for t in np.arange(0,tempo):
	del_E = 0
	for n in np.arange(0, N):
		i = int(np.random.random_sample()*N)
		x = int(i%L)
		y = int((i - i%L)/L)
		
		up = int((y-1+L)%L)
		down = int((y+1)%L)
		left = int((x-1+L)%L)
		right = int((x+1)%L)

		del_E = 2*S[x][y]*(S[x][up] + S[x][down] + S[left][y] + S[right][y])

		if del_E <= 0 or np.random.random_sample() < np.exp(-del_E/T):
			S[x][y] = -1*S[x][y]

	mag[t] = np.sum(S)

x = np.arange(0,tempo)
y = mag
plt.plot(x,y)
plt.show()