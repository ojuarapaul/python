print ('----Soma 3----')
num1 = (input ('Digite o primeiro número e tecle Enter: '))
try:
    val1 = int(num1)
    print('Ok, ', val1)
except ValueError:
    print('Você não digitou um número')
num2 = (input ('Digite o segundo número e tecle Enter: '))
try:
    val2 = int(num2)
    print('Ok, ', val2)
except ValueError:
    print('Você não digitou um número')
print ('O resultado dessa adição é: ', val1+val2)



