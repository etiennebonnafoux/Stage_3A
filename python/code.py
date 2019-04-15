import numpy as np
import matplotlib.pyplot as pl

def change_coordone(x,y,z):
    s=(x+y+z)
    x,y,z=x/s,y/s,z/s
    return (x+z*(0.5),z)

def trace_triangle():
    pl.clf()
    pl.plot([0,1],[0,0],[0,0.5],[0,1],[0.5,1],[1,0])

def iteration(a,b,c):
    d,e,f=0,0,0
    if a>c:
        d,e,f=a-c,c,b
        j=1
    else:
        d,e,f=b,a,c-a
        j=2
    return d,e,f,j

def execut(n):
    trace_triangle()
    a,b,c=1,np.pi,np.e
    Ma=np.array([[1,1,0],[0,0,1],[0,1,0]])
    Mb=np.array([[0,1,0],[1,0,0],[0,1,1]])
    xlist=[]
    ylist=[]
    jlist=[]
    for i in range(1,n):
        (x,y)=change_coordone(a,b,c)
        xlist.append(x)
        ylist.append(y)
        a,b,c,j=iteration(a,b,c)
        jlist.append(j)
    M=calcul_matrice(jlist)
    pl.scatter(xlist,ylist)
    print(M)

execut(50)

def calcul_matrice(jlist):
    M=np.eye(3)
    for i in range(len(jlist)):
        if jlist[i]==1:
            M=np.dot(M,Ma)
        else :
            M=np.dot(M,Mb)
    return M

# TODO : calculer les mineurs de tailles deux
# TODO : estimer les exposants de Lyoupanov
