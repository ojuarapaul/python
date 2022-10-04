print('CALCULADOR DE POTÊNCIAS DE NÚMEROS INTEIROS\n')
import math
#cria uma lista chamada listaPotencia
listaPotencia=[]
#dá entrada nas variáveis base, expoente1 e 2 e incremento
base=int(input('Digite a base: '))
expoente1=int(input('Digite o primeiro expoente: '))
expoente2=int(input('Digite o último expoente: '))
incremento=int(input('Digite o incremento entre os expoentes: '))
#cria a lista listaN
listaN=[]

#listaN será uma lista inicializada
#com uma sequência baseada nas variáveis dos expoentes.
#O objetivo é criar uma lista com todos os expoentes
#A instrução FOR percorre todos esses elementos (Dentro do RANGE explicado a seguir),
#um por vez e, em cada caso, atribui o valor do item à variável n
#observe que a função RANGE (A,B,C) retorna uma série numérica de inteiros, com inicio (A),
#fim (B) e incremento (C), variáveis já definidas anteriormente.

for n in range(expoente1,(expoente2+1),incremento):
    #append cria a listaN, baseada no Range estabelecido.
    listaN.append(n)
    #LEN retorna o tamanho (quantidade de números) da listaN, usado na impressão como parâmetro final do último RANGE
    p=len(listaN)
    #A variavel y realiza a operação de potenciação entre a variável base e as potencias criadas com o FOR
    #e armazenadas na listaN
    y=math.pow(base,(n))
    #cria a listaPotencia dos resultados das operações em y
    listaPotencia.append(y)
print('\nSerão usados',p,'expoentes')
print('Os expoentes usados serão',listaN)
print('Os resultados são',listaPotencia)
print('\nAs potências de',base,'a partir de',base,'elevado a',expoente1,'até',base,'elevado a',expoente2)
print('com incremento de',incremento,'entre os expoentes, são:')
#cria um loop para cada x de zero a 
for x in range(0,p):
    #listaN[x] pega os números armazenados em listaN, no range 0 a p (definido acima como o tamnho absoluto da listaN)
    #e lista no print abaixo
    print(base,'elevado a',listaN[x],'=',listaPotencia[x])

