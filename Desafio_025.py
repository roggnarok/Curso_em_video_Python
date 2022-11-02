#025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = input('Digite o nome completo: ').upper()

 #Abaixo, faz a verificação em cada bloco da variável splitada, se tem a palavra SILVA. Se tiver armazena true na variável, se não tiver armazena False. Variável é do tipo booleana.

temSilva = 'SILVA' in nome.split() #executo o teste para verificar se existe SILVA em alguns dos itens da lista criada.
if temSilva == True:    #Se a variável é igual a True, então:
    print('O nome possui a palavra SILVA!')
else:
    print(print('O nome NÃO possui a palavra SILVA!'))
#This job was made by Rodrigo. https://github.com/roggnarok