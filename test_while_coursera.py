sequência = []
decrescente = True
anterior = int(input('Digite o primeiro número da sequência: '))
valor = 1
while valor != 0  and decrescente:
    valor = int(input('Digite o próximo número da sequência: '))
    if valor > anterior:
        decrescente = False
    sequência.append (valor)
    anterior = valor
if decrescente == True:
    print('\nA sequência',sequência,'é decrescente')
else:
    print('\nOOPS!!!A sequência',sequência,'que você digitou é crescente')
               
