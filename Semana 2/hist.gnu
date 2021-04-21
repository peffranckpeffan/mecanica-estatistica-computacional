bw=0.01 #largura bin
N=10000 #num ptos
bin(x,bw)=bw*floor(x/bw) + bw/2.
norma=1./N/bw
p 'tst' u (bin($1,bw)):(norma) smooth freq with boxes