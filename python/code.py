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
    xlist=[]
    ylist=[]
    jlist=[]
    rho=[]
    denominateur=[]
    Ma=np.array([[1,1,0],[0,0,1],[0,1,0]])
    Mb=np.array([[0,1,0],[1,0,0],[0,1,1]])
    M=np.eye(3)
    for i in range(1,n):
        (x,y)=change_coordone(a,b,c)
        xlist.append(x)
        ylist.append(y)
        a,b,c,j=iteration(a,b,c)
        jlist.append(j)
        if j==1:
            M=np.dot(M,Ma)
        else :
            M=np.dot(M,Mb)
        P,Q,R=calcul_mineur(M)
        rho.append(max(np.abs(Q),np.abs(R))/max(M[0,1],1))
        denominateur.append(max(M[0,1],1))
    #pl.scatter(xlist,ylist)
    print(M)
    print(denominateur)
    #print(rho)
    #print(denominateur)
    #pl.plot(denominateur)
    pl.plot(rho[100:])

execut(140)

def calcul_matrice(jlist):
    for i in range(len(jlist)):
        if jlist[i]==1:
            M=np.dot(M,Ma)
        else :
            M=np.dot(M,Mb)
    return M

def calcul_mineur(M):
    P=M[0:2,0:2]
    Q=M[0:2,1:3]
    R=M[0:2,0:3:2]
    return (np.linalg.det(P),np.linalg.det(Q),np.linalg.det(R))

calcul_mineur(Mb)
Mb=np.array([[0,1,0],[1,0,0],[0,1,1]])
Mb
P=Mb[0:2,0:3:2]
print(P)
Mb[1,2]

# TODO : estimer les exposants de Lyoupanov
