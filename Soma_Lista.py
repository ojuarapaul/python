inputNum = []
inputNum = input('Digite até 4 números inteiros separado por traços')
lista = inputNum.split('-')
if len(lista) > 4:
    print('Você digitou mais de 4 números')
else:
    sum = 0
    for num in lista:
        sum = sum + int(num)
    print('A soma dos números é = ', sum)
