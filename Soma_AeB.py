#def main ()

# escreva o seu programa
print ('\nEsse programa soma dois números diferentes de zero')
a = int(input('digite a : '))
b = int(input('digite b : '))
while a==0:
    print ('a tem que ser diferente de zero')
    break
while b==0:
    print ('b tem que ser diferente de zero')
    break
if (a!=0) and (b!=0):
    print ('o resultado de ', a, '+', b, 'é', a+b)
else:
    print ('Você não leu o que está escrito???')
    
#main ()
