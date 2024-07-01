while True:
    print("O que deseja fazer?")
    print("0.Sair")
    print("1.Somar")
    print("2.Subtrair")
    print("3.Multiplicar")
    print("4.Dividir")
    option = int(input())

    if option == 0:
        exit()
    elif option == 1:
        number1 = int(input('Digite o Primeiro Número: '))
        number2 = int(input('Digite o Segundo Número: '))
        print('Resposta dessa soma é: ', number1 + number2)
    elif option == 2:
        number1 = int(input('Digite o Primeiro Número: '))
        number2 = int(input('Digite o Segundo Número: '))
        print('Resposta dessa subtração é: ', number1 - number2)
    elif option == 3:
        number1 = int(input('Digite o Primeiro Número: '))
        number2 = int(input('Digite o Segundo Número: '))
        print('Resposta dessa multiplicação é: ', number1 * number2)
    elif option == 4:
        number1 = int(input('Digite o Primeiro Número: '))
        number2 = int(input('Digite o Segundo Número: '))
        print('Resposta dessa divisão é: ', number1/number2)