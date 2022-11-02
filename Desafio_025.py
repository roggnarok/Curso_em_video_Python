#025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = input('Digite o nome completo: ') #Recebe o nome
nome = nome.upper() #Converte em maiúsculo e armazena na variável

 #Abaixo verifica se na variável nome tem a palavra SILVA. Se tiver armazena true na variável, se não tiver armazena False. Variável booleana.
temSilva = 'SILVA' in nome
if temSilva == True:    #Se a variável é igual a True, então:
    print('O nome possui a palavra SILVA!')
else:
    print(print('O nome NÃO possui a palavra SILVA!'))
#This job was made by Rodrigo. https://github.com/roggnarok