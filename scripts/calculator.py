def obter_numero(texto=''):
    while True:
        resposta = input(texto)
        if resposta.isdigit():
            return int(resposta)
        else:
            print("Isso não é um numero.")
while True:
    print("O que deseja fazer?")
    print("0.Sair")
    print("1.Somar")
    print("2.Subtrair")
    print("3.Multiplicar")
    print("4.Dividir")
    option = obter_numero()

#Fechar o código após digitar zero
    if option == 0:
        exit()

# Soma
    elif option == 1:
        number1 = obter_numero('Digite o Primeiro Número: ')
        number2 = obter_numero('Digite o Segundo Número: ')
        print('Resposta dessa soma é: ', number1 + number2) 

# Subtração
    elif option == 2:
        number1 = obter_numero('Digite o Primeiro Número: ')
        number2 = obter_numero('Digite o Segundo Número: ')
        print('Resposta dessa subtração é: ', number1 - number2) 

# Multiplicação
    elif option == 3:
        number1 = obter_numero('Digite o Primeiro Número: ')
        number2 = obter_numero('Digite o Segundo Número: ')
        print('Resposta dessa multiplicação é: ', number1 * number2) 

# Divisão
    elif option == 4:
        number1 = obter_numero('Digite o Primeiro Número: ')
        number2 = obter_numero('Digite o Segundo Número: ')
        if number2 == 0:  ## I2f para impedir a quebra do código com divisões por zero
            print('Não é possível realizar divisão por zero.')
            continue
        print('Resposta dessa divisão é: ', number1 / number2) 
        
    else:
        print('Esse valor é inválido, coloque um valor de acordo com as intruções.')