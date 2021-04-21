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
sumFreeZ_arr = np.zeros(np.arange(T_min, T_max, T_step).size)
E_m = np.zeros(np.arange(T_min, T_max, T_step).size)

def Z(T, S):
	return np.exp(-(1/T)*energia(S))

def energia(S):
	return -2*( S[0]*(S[1]+S[2]) + S[3]*(S[1]+S[2]) )

def magnetizacao(S):
	return np.sum(S)

for T in np.arange(T_min, T_max, T_step):
	sumZ = 0
	sumFreeZ = 0
	sumE_m = 0
	i = int(T*(1/T_step))
	for S[0] in np.arange(-1, 2, 2):
		for S[1] in np.arange(-1,2,2):
			for S[2] in np.arange(-1,2,2):
				for S[3] in np.arange(-1,2,2):
					
					sumZ += Z(T, S)
					
					sumFreeZ += (-T*np.log(sumZ))

	sumFreeZ_arr[i] = sumFreeZ/N

x = np.arange(T_min, T_max, T_step)
y = sumFreeZ_arr
plt.plot(x, y)
#plt.plot(x, y1)
#plt.ylim(-3.6,-2.8)
#plt.xlim(0,5)
plt.ylabel('Energia Livre')
plt.xlabel('T')
plt.show()