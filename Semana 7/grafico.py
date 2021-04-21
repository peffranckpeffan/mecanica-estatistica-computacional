import numpy as np
import matplotlib.pyplot as plt

T = 2
tempo = 6000

L = 100
N = L*L

S = np.ones(N, dtype=int)
S = 2*np.random.randint(2, size=N)-1
mag = np.zeros(tempo, dtype=int)

for t in np.arange(0,tempo):
	del_E = 0
	for n in np.arange(0, N):
		i = int(np.random.random_sample()*N)
		x = i%L
		y = (i - i%L)/L

		del_E = 2*S[int(i)]*(S[int(x + L * ((y+1)%L))] + S[int(((x+1)%L) + L * y)] )

		if del_E <= 0 or np.random.random_sample() < np.exp(-del_E/T):
			S[i] = -S[i]

	mag[t] = np.sum(S)*np.exp(-del_E/T)

y = mag
x = np.arange(0,tempo)
plt.plot(x,y)
plt.show()
		
