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
E_m = np.zeros(np.arange(T_min, T_max, T_step).size)

def Z(T, S):
	return np.exp(-(1/T)*energia(S))

def energia(S):
	return -2*( S[0]*(S[1]+S[2]) + S[3]*(S[1]+S[2]) )

for T in np.arange(T_min, T_max, T_step):
	sumZ = 0
	sumE_m = 0
	for S[0] in np.arange(-1, 2, 2):
		for S[1] in np.arange(-1,2,2):
			for S[2] in np.arange(-1,2,2):
				for S[3] in np.arange(-1,2,2):
					sumZ = sumZ + Z(T, S)
					sumE_m = sumE_m + energia(S)*Z(T, S)
					E_m[int(T*(1/T_step))] = sumE_m/sumZ/N

x = np.arange(T_min, T_max, T_step)
y = E_m
plt.plot(x, y)
plt.ylim(-2,-0.8)
plt.xlim(0,5)
plt.ylabel('<e>')
plt.xlabel('T')
plt.show()