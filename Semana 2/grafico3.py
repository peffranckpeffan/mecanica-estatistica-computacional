import numpy as np 
import matplotlib.pyplot as plt
p=.5
n=1
M=10000
nbins=10
def subparte3(N):
    histograma = np.zeros(nbins, dtype=np.int)
    dk = 1./nbins

    for i in range(M):
        med = 0
        for j in range(1,N+1):
            for k in range(n):
                suc = 0
                s = np.random.random()
                if s < p:
                    suc += 1
            med += suc
        med /= N
        for l in range(nbins):
            if ((l*dk < med) and (med <= (l+1)*dk)):
                histograma[l] += 1
    return histograma, dk

for m in range(3):
    N = [10,100,1000][m]
    histograma, dk = subparte3(N)
    soma = np.sum(histograma)
    x = np.linspace(0+dk/2,1+dk/2,nbins,endpoint=False)
    plt.subplot(1,3,m+1)
    plt.bar(x, histograma/soma, width=1*dk)
    plt.text(0,max(histograma)/soma, f"N = {N}")

#plt.suptitle(f"Histogramas da média amostral de uma distribuição de Bernoulli.\nM = {M} histórias.")
#plt.savefig("semana02c.png", dpi=400)
plt.show()