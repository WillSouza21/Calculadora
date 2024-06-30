print("O que deseja fazer?")
print("0.Sair")
print("1.Somar")
print("2.Subtrair")
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