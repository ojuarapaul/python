inputNum = []
inputNum = input('Digite até 4 números inteiros separado por traços')
lista = inputNum.split('-')
while len(lista) < 5:
    sum = 0
    for num in lista:
        sum = sum + int(num)
    print('A soma dos números é = ', sum)
    break
if len(lista) >=5:
    print('você digitou mais de 4 números')
else:
    print ('fim do programa')