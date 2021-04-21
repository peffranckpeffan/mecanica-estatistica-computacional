#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

# PARTE 1 #
def parte1(p=.5, n=5, M=10000):
    histograma = np.zeros(n+1,dtype=np.int)
    for his in range(M):
        count = 0
        for i in range(n):
            s = np.random.random()
            if s < p:
                count += 1
        histograma[count] += 1

    plt.plot()
    plt.xlabel("n")
    plt.bar(range(n+1),histograma/float(M))
    #plt.text(-.4,max(histograma/float(M)), f"{M} histórias \np = {p}", va="top")
    #plt.title(f"Distribuição Binomial p/ N = {n}")
    #plt.savefig("semana02a.png", dpi=400)
    plt.show()

# PARTE 2 #
def parte2(p=.5, n=1, N=1000):
    sigma = np.zeros(N)

    med  = 0
    med2 = 0
    for i in range(1,N+1):
        suc = 0
        for j in range(n):
            s = np.random.random()
            if s < p:
                suc += 1
        med += suc
        med2 += suc**2
        k2med = med2/i
        kmed2 = pow(med/i,2)
        if i-1 != 0:
            sigma[i-1] = pow((k2med-kmed2)/(i-1), .5)
        else: 
            sigma[i-1] = None
    
    x = range(2,N)
    sigma = np.delete(sigma, [0,1])
    plt.plot(x,sigma, "-r", lw=0.6)
    plt.xlabel("N")
    plt.ylabel(r"$\sigma_N$")
    #plt.title("Erro do estimador")
    #plt.savefig("semana02b.png", dpi=400)
    plt.show()

# PARTE 3 #
def parte3(p=.5, n=1, M=10000, nbins=10):
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

def __main__():
    #parte1()
    #parte2()
    parte3()

__main__()
