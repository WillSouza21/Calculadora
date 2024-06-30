print("O que deseja fazer?")
print("0.Sair")
print("1.Somar")
option = int(input())

if option == 0:
    exit()
elif option == 1:
    number1 = int(input('Digite o Primeiro Número: '))
    number2 = int(input('Digite o Segundo Número: '))
    print('Resposta dessa soma é: ', number1 + number2)
    