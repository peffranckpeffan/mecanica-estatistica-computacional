import numpy as np 
import matplotlib.pyplot as plt
import math as mt
import pprint as pp

L = 2
N = L*L
T_min = 0.000000001
T_max = 5.1
T_step = 0.1

S = np.zeros(N, dtype=int)
m_arr = np.zeros(np.arange(T_min, T_max, T_step).size)
m_arr2 = np.zeros(np.arange(T_min, T_max, T_step).size)
chi = np.zeros(np.arange(T_min, T_max, T_step).size)

def Z(T, S):
	return np.exp(-(1/T)*energia(S))

def energia(S):
	return -2*( S[0]*(S[1]+S[2]) + S[3]*(S[1]+S[2]) )

def magnetizacao(S):
	return np.sum(S)

for T in np.arange(T_min, T_max, T_step):
	sumZ = 0
	summ = 0
	summ2 = 0
	for S[0] in np.arange(-1, 2, 2):
		for S[1] in np.arange(-1,2,2):
			for S[2] in np.arange(-1,2,2):
				for S[3] in np.arange(-1,2,2):
					
					sumZ = sumZ + Z(T, S)
					
					summ = summ + abs(magnetizacao(S))*Z(T, S)
					summ2 = summ2 + abs(magnetizacao(S))*abs(magnetizacao(S))*Z(T, S)

					i = int(T*(1/T_step))

					m_arr[i] = summ/sumZ/N
					m_arr2[i] = summ2/sumZ/N/N

					chi[i] = ((m_arr2[i]-m_arr[i]*m_arr[i])*N)/T

x = np.arange(T_min, T_max, T_step)
y = chi
y1 = m_arr
plt.plot(x, y)
#plt.plot(x, y1)
plt.ylim(0,0.2)
plt.xlim(0,5)
plt.ylabel('suscetibilidade')
plt.xlabel('T')
plt.show()