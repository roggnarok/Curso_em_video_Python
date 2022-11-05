''' Desafio 28
Escreva um programa que faça o computador gerar um número inteiro entre 0 e 5, peça para o usuário tenar adivinhar qual foi o número gerado pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu
'''
from random import randint
from time import sleep
numeroPC = randint(0,5) #PC escolhe aleatóriamente entre os números 0 e 5
numeroUsuario = -1
while numeroUsuario < 0 or numeroUsuario > 5: #Enquanto o usuário digite nº <0 ou >5:
    numeroUsuario = int(input('Qual número entre 0 e 5 você acha que o computador escolheu? ')) #Usuário tenta adivinhar
print('PROCESSANDO...')
sleep(1.2)
if numeroPC == numeroUsuario :
    print(f'Você acertou!')
else:
    print(f'Você errou!')
print(f'O número escolhido pelo PC foi {numeroPC}.')
#This job was made by Rodrigo. https://github.com/roggnarok