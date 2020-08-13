from random import randint

def echantillon(n):
    c=0
    for i in range(n):
        x=randint(1,6)
        if (x==1):
            c=c+1
    return(c/n)

def simulation(N,n):
    L=[]
    for i in range(N):
        f=echantillon(n)
        L.append(f)
    return(L)


