print('Sistema de Cadastro Simples (em memória)')

adicionar_nome = []
adicionar_idade = []
adicionar_email = []

usuarios = [adicionar_nome, adicionar_idade, adicionar_email]


continuar = True
while continuar == True:
    print('-----------------------------')
    print('[1] -> Cadastrar novo usuário')
    print('[2] -> Ver lista de usuários')
    print('[3] -> Remover usuário')
    print('[4] -> Sair do programa')
    print('-----------------------------')

    escolha = int(input('O que você quer fazer agora?: '))
    
    if escolha == 1:
        novo_nome = str(input('Digite o nome: '))
        nova_idade = int(input('Digite a idade: '))
        novo_email= str(input('Digite o email: '))

        if novo_email not in adicionar_email:
            adicionar_nome.append(novo_nome)
            adicionar_idade.append(nova_idade)
            adicionar_email.append(novo_email)
            print('Usuário cadastrado!')
        else:
            print('Usuário não cadastrado, esse e-mail já consta no sistema.')


    elif escolha == 2:
        for i in range(len(usuarios)):
            print(f'{usuarios[i]}\n')
    elif escolha == 3:
        print('---Para remover um usuários, escolha baseado na posição dele, começa em 0!---')
        print(usuarios)
        remover = int(input('Digite o n° da posição para remover: '))
        del adicionar_nome[remover]
        del adicionar_idade[remover]
        del adicionar_email[remover]
    elif escolha == 4:
        continuar = False