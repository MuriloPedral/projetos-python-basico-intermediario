print('---Bem-Vindo! Simulador de saque de um caixa eletrônico---')

CEDULAS = [100, 50, 20, 10, 5, 2]
n100 = 0
n50 = 0
n20 = 0
n10 = 0
n5 = 0
n2 = 0
valor_f = 1

quer_sacar = int(input('Gostaria de realizar um saque? [1] para sim e [2] para não: '))

if quer_sacar == 1:
    print(f'Cédulas disponíveis: R${CEDULAS[0]}, R${CEDULAS[1]}, R${CEDULAS[2]}, R${CEDULAS[3]}, R${CEDULAS[4]}, R${CEDULAS[5]}')
    valor = int(input('Digite o valor a ser sacado: R$'))

    while valor >= CEDULAS[5]:
        if valor >= CEDULAS[0]:
            valor = valor - CEDULAS[0]
            n100 = n100 + 1
        elif valor >= CEDULAS[1]:
            valor = valor - CEDULAS[1]
            n50 = n50 + 1
        elif valor >= CEDULAS[2]:
            valor = valor - CEDULAS[2]
            n20 = n20 + 1
        elif valor >= CEDULAS[3]:
            valor = valor - CEDULAS[3]
            n10 = n10 + 1
        elif valor >= CEDULAS[4]:
            valor = valor - CEDULAS[4]
            n5 = n5 + 1
        elif valor >= CEDULAS[5]:
            valor = valor - CEDULAS[5]
            n2 = n2 + 1
        
        valor_f = valor

    if valor_f == 0:
        print(f'Saque: {n100} x R${CEDULAS[0]}, {n50} x R${CEDULAS[1]}, {n20} x R${CEDULAS[2]}, {n10} x R${CEDULAS[3]}, {n5} x R${CEDULAS[4]}, {n2} x R${CEDULAS[5]}')
    else:
        print('O valor digitado não consegue ser sacado, vamos reiniciar o sistema.')  

elif quer_sacar == 2:
    print('Obrigado pela paciência!')
else:
    print('Você digitou um valor inválido, vamos fechar o sistema.')