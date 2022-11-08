'''
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a conversão.
'''
numero = int(input('Digite um número inteiro: '))

conversao = int(-1)
while (conversao < 1) or (conversao > 3):
    conversao = int(input('Digite um código para a conversão:\
    \n[1] - Binário\
    \n[2] - Octal\
    \n[3] - Hexadecimal\
    \n\tSua opção: '))

if conversao == 1:
    print(f'O valor digitado {numero}, convertido em Binário é {bin(numero)[2:]}') 
    #[2:] faz o fatiamento da string e mostra a partir do índice 2 até o final.
elif conversao == 2:
    print(f'O valor digitado {numero}, convertido em Octal é {oct(numero)[2:]}')
elif conversao == 3:
    print(f'O valor digitado {numero}, convertido em Hexadecimal é {hex(numero)[2:]}')
#This job was made by Rodrigo. https://github.com/roggnarok