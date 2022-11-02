#024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
cidade = input('Digite o nome de uma cidade: ').upper().strip() #Recebe o nome, converte em maiúsculo, limpa os espaços no ínicio e no final da string e armazena na variável cidade.
nomeCidadeFatiado = cidade.split() #Fatia o nome da cidade e armazena na variável.

#Caso a cidade começe com o nome SANTO, esse nome deve estar armanzenado no índice zero da variável nomeCidadeFatiado.
#Para evitar que pavras como Santos e Santoo acusem errôneamente que o nome da cidade começa com SANTO, na verificação, incluí um espaço após o nome SANTO_
if 'SANTO ' in nomeCidadeFatiado[0]: #Se no índice zero(0) da variável contiver o nome 'SANTO', então:
    print('A cidade começa com SANTO') #Imprime que o nome da cidade começa com SANTO
else:                                   #Em caso negativo, faça:
    print('A cidade NÃO começa com SANTO') #Imprime que o nome da cidade não começa com SANTO
#This job was made by Rodrigo. https://github.com/roggnarok