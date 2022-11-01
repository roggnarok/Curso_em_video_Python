#022: Crie um programa que leia o nome completo de uma pessoa e mostre: - O nome com todas as letras maiúsculas e minúsculas. - Quantas letras ao todo (sem considerar espaços). - Quantas letras tem o primeiro nome.
nome = input('Digite um nome completo: ')
nome = nome.strip() # Remove os espaços antes e após o nome
maiuscula = nome.upper() #Transmorma tudo em maiúscula e guarda na variável
minuscula = nome.lower() #Transmorma tudo em minúscula e guarda na variável
nomeFatiado = nome.split() #Faz o fatiamento das partes do nome e guarda na variável
primeiroNome = nomeFatiado[0] #Guarda na variável primeiroNome o valor que consta no índice 0 da variável nomeFatiado
tamanho = len(nome) #armazena o valor (int) da quantidade de caracter do tamanho do nome
espacos = nome.count(' ') #Conta quatos espaços exitem na variável nome e armazer a quantidade de espaços
nroDeLetras = tamanho - espacos #subtração da qtd de caracteres do nome, menos a quantidade de espaços
print(f'O nome convertido em maiúscula é {maiuscula}\
    \nO nome converido em minúscula é {minuscula}\
    \nEste nome tem {nroDeLetras} letras, sem considerar os espaços.\
    \nO primeiro nome tem {len(primeiroNome)} letras.')
#This job was made by Rodrigo. https://github.com/roggnarok
