'''
Jokenpô (Pedra, Papel e Tesoura)
'''
placarPC = 0        #Contador para o placar do computador
placarUsuario = 0   #Contador para o placar do usuário
while True:    
    import random
    escolhas = ['pedra', 'papel', 'tesoura'] #Cria a lista de opções
    computador = random.choice(escolhas) #PC escolhe uma das opções e salva na variável
    
    usuario = None #Variável usuario é inicializada
    while usuario not in escolhas: #Enquanto a variável usuário não estiver dentro das opções da variável escolhas, continue:
        usuario = input('Pedra, Papel ou Tesoura? ').lower().strip() #usuário digita a opção, essa opção é convertida em minúsculo e é eliminado os espaços em branco.
    def mostraEscolhas():
        print(f'Computador escolheu {computador}.')
        print(f'Usuário escolheu {usuario}.')

    if computador == usuario:
        mostraEscolhas()
        print('Empatou!')

    elif usuario == 'pedra':
        if computador == 'papel':
            mostraEscolhas()
            print('Você perdeu!')
            placarPC += 1
        if computador == 'tesoura':
            mostraEscolhas()
            print('Você ganhou!')
            placarUsuario += 1

    elif usuario == 'tesoura':
        if computador == 'papel':
            mostraEscolhas()
            print('Você ganhou!')
            placarUsuario += 1
        if computador == 'pedra':
            mostraEscolhas()
            print('Você perdeu!')
            placarPC += 1

    elif usuario == 'papel':
        if computador == 'tesoura':
            mostraEscolhas()
            print('Você perdeu!')
            placarPC += 1
        if computador == 'pedra':
            mostraEscolhas()
            print('Você ganhou!')
            placarUsuario += 1

    #Mostra o placar
    print(f'\033[0;30;45m\tPLACAR\033[m\
        \n\033[0;30;42m>>> VOCÊ {placarUsuario} x {placarPC} COMPUTADOR <<<\033[m')
    #O código \033[0,30;45m mostra o PLACAR na cor Preta e o fundo em lilás
    #O código \033[31;47m mostra na cor Vermelha e o fundo em Cinza
    #jogo acaba quando alguém fizer 3 pontos
    if placarUsuario == 3:
        print('Você venceu o computador!')
        break
    elif placarPC == 3:
        print('Você perdeu do computador!')
        break
    jogarNovamente = input('Jogar de novo? (S/N): ').upper().strip()

    if jogarNovamente == 'N':
        break
#This job was made by Rodrigo. https://github.com/roggnarok
