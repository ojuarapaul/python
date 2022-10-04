import random
import math
#a=random.randint(1,10)
a=int(input('digite a :'))
x=pow (2,a)
print('2 elevado a',a,'=',x)
y=math.sqrt(x)
print(type(y))
if type(y) is int:
    z=int(y)
    print('e a raiz quadrada de',x,'é =',z)
else:
    print('e a raiz quadrada de',x,'É =',round (y,2))
