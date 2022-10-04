# Definição dos parâmetros n e k pelo usuário
print('\nCÁLCULO DO COEFICIENTE BINOMIAL DE (n,k)')
n = int(input('\ndigite n '))
k = int(input('digite k '))


# Definição da função que calcula o fatorial de um número 
def fat0(x):
    i = 1
    Xfat = 1
    for n in range (1,x+1):
        Xfat = Xfat * i 
        i = i + 1
    return Xfat

#Esta função pega os parâmetros n e k
def fat(n,k):
    # e retorna a variável Nfat como sendo o fatorial de n,
    # que é calculado pela função fat0 definida no início
    Nfat = fat0(n)
    # mesma coisa com a variável Kfat
    Kfat = fat0(k)
    #mesma coisa com (n-k)!
    Pfat = (n-k)
    Pfat = fat0(Pfat)
    # bn calcula o coeficiente binomial
    print('\nn!= ',Nfat)
    print('k!= ',Kfat)
    print('(n-k)!= ',Pfat)
    bn = Nfat / (Kfat*Pfat)
    print('a resposta é ',int(bn))

    #mas uma opção melhor é fazer direto mesmo:
    z = fat0(n) / (fat0(k) * fat0(n-k))
    print('\nO coeficiente binomial de n=',n,'e k=',k,'é',int(z))

if n<k:
    print('\nn tem que ser um número Natural e maior ou iqual a k')
    print('a operação não pôde ser completada')
else:
    fat(n,k)


