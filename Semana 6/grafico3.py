import numpy as np 
import matplotlib.pyplot as plt
import math as mt
import pprint as pp

L = 2
N = L*L
T_min = 0.00001
T_max = 5.1
T_step = 0.1

S = np.zeros(N, dtype=int)
m_arr = np.zeros(np.arange(T_min, T_max, T_step).size)
E_m = np.zeros(np.arange(T_min, T_max, T_step).size)
E_m2 = np.zeros(np.arange(T_min, T_max, T_step).size)
Cv = np.zeros(np.arange(T_min, T_max, T_step).size)

def Z(T, S):
	return np.exp(-(1.0/T)*energia(S))

def energia(S):
	return -2*( S[0]*(S[1]+S[2]) + S[3]*(S[1]+S[2]) )

def magnetizacao(S):
	return np.sum(S)

for T in np.arange(T_min, T_max, T_step):
	sumZ = 0
	sumE_m = 0
	sumE_m2 = 0

	i = int(T*(1/T_step))
	
	for S[0] in np.arange(-1, 2, 2):
		for S[1] in np.arange(-1,2,2):
			for S[2] in np.arange(-1,2,2):
				for S[3] in np.arange(-1,2,2):
					
					sumZ = sumZ + Z(T, S)

					sumE_m += energia(S)*Z(T, S)
					sumE_m2 += energia(S)*energia(S)*Z(T, S)
	
	E_m[i] = sumE_m/sumZ/N
	E_m2[i] = sumE_m2/sumZ/N/N

	Cv[i] = ((E_m2[i]-E_m[i]*E_m[i])*N)/(T*T)

x = np.arange(T_min, T_max, T_step)
y = Cv
plt.plot(x, y)
plt.ylim(0,0.5)
plt.xlim(0,5)
plt.ylabel('Cv')
plt.xlabel('T')
plt.show()