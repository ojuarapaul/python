print('CALCULADOR DE POTÊNCIAS DE NÚMEROS INTEIROS\n')
import math
listaPotencia=[]
base=int(input('Digite a base: '))
expoente1=int(input('Digite o primeiro expoente: '))
expoente2=int(input('Digite o último expoente: '))
incremento=int(input('Digite o incremento entre os expoentes: '))
listaN=[]
for n in range(expoente1,(expoente2+1),incremento):
    listaN.append(n)
    p=len(listaN)
    y=math.pow(base,(n))
    listaPotencia.append(y)
print('\nAs potências de',base,'a partir de',base,'elevado a',expoente1,'até',base,'elevado a',expoente2)
print('com incremento de',incremento,'entre os expoentes, são:')
for x in range(0,p):    
    print(base,'elevado a',listaN[x],'=',listaPotencia[x])

