#import string
import variaveis_constante

#LCARAC_ESPECIAL = list(string.punctuation)
print('---Validador de Senha---')
print('---Sua senha deve conter 1 letra, 1 número e um caractere especial \n---Com pelo menos 6 dígitos e no máximo 12.')

print('---LISTA DOS CARACTERES ESPECIAIS---')
print(variaveis_constante.CARACTERES_ESPECIAIS)

senha = list(str(input('Digite sua senha: ')))
tamanho = len(senha)

if tamanho < 6 or tamanho > 12:
    print('Senha inválida, número ideal de caracteres não atingido')
    reiniciar = str(input('Quer tentar mais uma vez? (s/n)')).lower()
    if reiniciar == 's':
        senha = list(str(input('ÚLTIMA TENTAIVA!\n Digite a nova senha: ')))
        tamanho = len(senha)
        if tamanho < 6 or tamanho > 12:
            print('Número de caracteres inválido, encerrando o programa...')
    elif reiniciar == 'n':
        print('Obrigado por utilizar o sistema!')
    else: 
        print('Você digitou algo diferente do esperado, estamos encerrando o programa...')

if tamanho >= 6 and tamanho <= 12:
    variaveis_constante.SENHA_VALIDA = True

if variaveis_constante.SENHA_VALIDA == True:
    for i in range(tamanho):
        for i2 in range(len(variaveis_constante.NUMEROS)):
            if senha[i] == variaveis_constante.NUMEROS[i2]:
                variaveis_constante.CONTAGEM_N = variaveis_constante.CONTAGEM_N + 1
        for i3 in range(len(variaveis_constante.LETRAS)):
            if senha[i] == variaveis_constante.LETRAS[i3]:
                variaveis_constante.CONTAGEM_L = variaveis_constante.CONTAGEM_L + 1
        for i4 in range(len(variaveis_constante.CARACTERES_ESPECIAIS)):
            if senha[i] == variaveis_constante.CARACTERES_ESPECIAIS[i4]:
                variaveis_constante.CONTAGEM_C = variaveis_constante.CONTAGEM_C + 1
    
    if variaveis_constante.CONTAGEM_C == 0 or variaveis_constante.CONTAGEM_L == 0 or variaveis_constante.CONTAGEM_N == 0:
        if variaveis_constante.CONTAGEM_C == 0:
            print('A sua senha não tinha caracteres especiais')
        
        if variaveis_constante.CONTAGEM_L == 0:
            print('A sua senha não tinha letras')
        
        if variaveis_constante.CONTAGEM_N == 0:
            print('A sua senha não tinha números')
    else:
        print(f'Parabéns sua senha foi alterada para: {"".join(senha)}')