def maior_primo(numero):
    x = 0
    resp = numero
    #checa se [numero] é primo
    for divisor in range(1,numero):
        if numero % divisor == 0:
            x = x + 1
            
    #se for, retorna [numero]
    if x == 1:
        resp = numero

    #se não for, executa ehprimo do número anterior [número -1]
    else:
        resp = maior_primo(numero - 1)
   
    return resp



