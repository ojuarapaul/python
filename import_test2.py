import random
import math
import sys
#a=random.randint(1,10)

def potencia (a):
    x=pow (2,a)
    print('2 elevado a',a,'=',x)
    y=math.sqrt(x)
    if y % 2 == 0:
        print('e a raiz quadrada de',x,'É =',int(y))
    else: 
        y=round (y,2)     
        print('e a raiz quadrada de',x,'é =',y)
    b=str(input('Deseja continuar? Y/N '))
    if b=='N' or b=='n':
        sys.exit()
    else:
        print('Let''s go!')
        init()
        
def init():
    print('Calcula a potencia de 2 de um número e a raiz quadrada do resultado')
    a=int(input('digite o número desejado :'))
    potencia(a)

init()
