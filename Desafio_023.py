#023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
numero = -1
while (numero < 0) or (numero > 9999): #Filtro para que o valor digitado esteja entre 0 e 9999
    numero = int(input('Digite um número entre 0 e 9999: '))

numero = str(numero) #Converte o nº digitado em uma string, para posterior tratamento
numero = numero.strip() #Remove os espaços no começo e no final da string
for i in range(0,len(numero)): #Para i valendo de 0 até o comprimento da string len(numero), faça:
    print(f'O {i+1}º número Digitado foi {numero[i]}') #Imprime cada um dos nº digitados de forma individual
#This job was made by Rodrigo. https://github.com/roggnarok