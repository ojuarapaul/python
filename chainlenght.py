print('CALCULADORA DE TAMANHO DE CORRENTE DA PARK TOOL')
print('by Paulo Araujo')
import math
def main():
    inicio=input('\nVocê deseja o tamanho da corrente em cm [c] ou polegadas [p] ou pela fórmula rigorosa [r]? ')
    if inicio==('c'):
        centimetros()
    elif inicio==('p'):
        polegadas()
    elif inicio==('r'):
        rigorosa()
               
def cont():
    brk=input ('\nDeseja continuar? Digite [n] para encerrar ou qualquer tecla para continuar -> ')
    if brk ==('n'):
        print('\nObrigado por usar nosso avançadíssimo sistema de cálculo de tamanho de correntes.')
    else: main()   

def centimetros():
    chainstay = float(input('Digite o tamanho do chainstain em polegadas, formato decimal - ex: 16.0, 17.5, 18.25 etc: '))
    largercog = int(input('Digite o numero de dentes da maior catraca - ex: 42: '))
    chainring = int(input('Digite o numero de dentes da sua maior - ou única - coroa - ex:30: '))
    a = (chainstay*2)
    b = (largercog/4)
    c = (chainring/4)
    chainLenght = a + b + c + 1
    lenghtCm = (chainLenght)*2.54
    lenghtResto=((lenghtCm)-int(lenghtCm))
    if lenghtResto < (0.50):
        chainLenghtCm = int(lenghtCm)
        chainLenght = int(chainLenght)
        numLinks = chainLenght*2
        print ('\nO tamanho da corrente é',chainLenghtCm,'cm ou',numLinks,'links')
    elif lenghtResto >= (0.50):
        chainLenghtCm = int(lenghtCm) + 1
        chainLenght = int(chainLenght)
        numLinks = chainLenght*2
        print ('\nO tamanho da corrente é',chainLenghtCm,'cm ou',numLinks,'links')
    print('Use a equação rigorosa SOMENTE se a bicicleta tiver uma coroa bem grande, uma catraca bem pequena e for single-speed')
    print('Além disso, a bike precisaria de um chainstay muito curto, tipo 15 polegadas ou menos')
    print('Se você usa um MissingLink, inclua-o quando for medir a corrente.')
    cont()

def polegadas():
    chainstay = float(input('digite o tamanho do chainstain em polegadas, formato decimal - ex: 16.0, 17.5, 18.25 etc: '))
    largercog = int(input('digite o numero de dentes da maior catraca - ex: 42: '))
    chainring = int(input('digite o numero de dentes da sua maior - ou única - coroa - ex:30: '))
    a = (chainstay*2)
    b = (largercog/4)
    c = (chainring/4)
    chainLenght = a + b + c + 1
    lenghtResto1=((chainLenght)-int(chainLenght))
    if lenghtResto1 < (0.50):
        chainLenght = int(chainLenght)
        numLinks = chainLenght*2
        print ('\nO tamanho da corrente é',chainLenght,'polegadas ou',numLinks,'links')
    elif lenghtResto1 >= (0.50):
        chainLenght = int(chainLenght) + 1
        numLinks = chainLenght*2
        print ('\nO tamanho da corrente é',chainLenght,'polegadas ou',numLinks,'links')
    print('Se você usa um MissingLink, inclua-o quando for medir a corrente.')
    cont()
 
def rigorosa():
    chainstay = float(input('digite o tamanho do chainstain em polegadas, formato decimal - ex: 16.0, 17.5, 18.25 etc: '))
    largercog = int(input('digite o numero de dentes da catraca - ex: 12: '))
    chainring = int(input('digite o numero de dentes da sua coroa - ex:58: '))
    c = (chainstay)
    r = (largercog)
    f = (chainring)
    x = 1+(f+r)/4
    y = (f-r)
    z = (0.0796*y)**2
    w = c**2
    k = math.sqrt (w+z)
    chainLenght = x + 2*k
    print(chainLenght)
    lenghtResto1=((chainLenght)-int(chainLenght))
    if lenghtResto1 < (0.50):
        chainLenght = int(chainLenght)
        numLinks = chainLenght*2
        print ('\nO tamanho rigoroso da corrente é',chainLenght,'polegadas ou',numLinks,'links')
    elif lenghtResto1 >= (0.50):
        chainLenght = int(chainLenght) + 1
        numLinks = chainLenght*2
        print ('\nO tamanho rigoroso da corrente é',chainLenght,'polegadas ou',numLinks,'links')
    print('Se você usa um MissingLink, inclua-o quando for medir a corrente.')
    cont()
main()
