print('\nEsse programa converte Farenheit em Celsius e vice-versa')
print('by Paulo Araujo - Dedicated to Sil & Teco')


def main():
    c2f=input('\nVocê deseja converter Celsius para Farenheit [c] ou Farenheit para Celsius [f] ')
    if c2f==('f'):
        C2F()
    elif c2f==('c'):
        F2C()
def cont():
    brk=input ('\nDeseja continuar? Digite [n] para encerrar ou qualquer tecla para continuar -> ')
    if brk ==('n'):
        print('\nObrigado por usar nosso avançadíssimo sistema de conversão. Have a nice day.')
        print('Esse programa é dedicado a Sil & Teco, que me inspiram em tudo que eu invento.\n')
    else: main()
def C2F():
    tempf=float(input('\ndigite a temperatura em Farenheit '))
    tempc=5*((tempf-32)/9)
    if tempc >= (-1) and tempc <= (1):
        print(tempf, (f'ºF é {tempc:.1f}'), ('ºC'))
        cont()
    else:
        print (tempf, (f'ºF são {tempc:.1f}'), ('ºC'))
        cont()
def F2C():
    tempc=float(input('\ndigite a temperatura em Celsius '))
    tempf=((9*tempc/5)+32)
    if tempf >= (-1) and tempf <= (1):
        print(tempc, (f'ºF é {tempf:.1f}'), ('ºC'))
        cont()
    else:
        print (tempc, (f'ºF são {tempf:.1f}'), ('ºC'))
        cont()
main()



   

