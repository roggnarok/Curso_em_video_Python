#024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
cidade = input('Digite o nome de uma cidade: ') 
cidade = cidade.upper() #converte em maísculo
nomeCidadeFatiado = cidade.split() #Fatia o nome da cidade e armazena na variável.

#Caso a cidade começe com o nome SANTO, esse nome deve estar armanzenado no índice zero da variável nomeCidadeFatiado.
if 'SANTO' in nomeCidadeFatiado[0]: #Se no índice zero(0) da variável contiver o nome 'SANTO', então:
    print('A cidade começa com SANTO') #Imprime que o nome da cidade começa com SANTO
else:                                   #Em caso negativo, faça:
    print('A cidade não começa com SANTO') #Imprime que o nome da cidade não começa com SANTO
#This job was made by Rodrigo. https://github.com/roggnarok