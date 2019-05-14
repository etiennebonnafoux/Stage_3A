import random
import matplotlib.pyplot as pl

def tirage_N():
  x=random.random()
  N=0
  while(x>0):
      x=x-(1/((N+1)*(N+2)))
      N+=1
  return (N-1)

def liste_N(iter):
    N=[]
    for i in range(iter):
        N.append(tirage_N())
    return N

def recurence(iter):
    Vect=[1,1,1]
    Beta=[1,1,1]
    N=liste_N(iter+5)
    for i in range(iter):
        Beta.append(-N[i]*Beta[-1]-Beta[-2]+Beta[-3])
        Vect.append(Vect[-1]+N[i]*Vect[-2]+Vect[-3])
    return(Beta,Vect)

def signeliste(Listee):
    T=[]
    for a in Listee:
        if a < 0 :
            T.append(0)
        else:
            T.append(1)
    return T

B,V=recurence(200)

print(B)

def dessin(iter):
    Beta,Vect=recurence(iter)
    T=[Beta[i]/Vect[i] for i in range(len(Beta))]
    pl.plot(T)
    #pl.plot(Beta,color='red')
    #pl.plot(Vect,color='green')
    pl.show()

dessin(20)
