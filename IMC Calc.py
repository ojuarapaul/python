print('\nEsse programa calcula o IMC')
print('by Paulo Araujo')
Peso = float(input('\nDigite seu peso em quilogramas - Ex: 46.7: '))
Altura = float(input('Digite sua altura em metros - Ex: 1.78: '))
IMC = Peso / (Altura ** 2 )
if IMC < (17):
    print('\nVocê está muito abaixo do peso - procure um endocrinologista e um nutricionista')
elif IMC >= (17) and IMC <=(18.49):
    print('\nVocê está abaixo do peso')
elif IMC >= (18.5) and IMC <=(24.99):
    print('\nVocê está com o peso normal. Continue se exercitando regularmente e comendo corretamente')
elif IMC >= (25) and IMC <=(29.99):
    print('\nVocê está acima do peso - procure um endocrinologista e um nutricionista')
elif IMC >= (30) and IMC <=(34.99):
    print('\nVocê está com Obesidade Grau I - procure um endocrinologista e um nutricionista')
elif IMC >= (35) and IMC <=(39.99):
    print('\nVocê está com Obesidade Grau II (severa) - procure um endocrinologista e um nutricionista')
elif IMC >= (40):
    print('\nVocê está com Obesidade Grau III (mórbida) - procure um endocrinologista e um nutricionista')
    
convertIMC = int(IMC)
print ('\nO seu Índice de Massa Corpórea é ',convertIMC)
      

