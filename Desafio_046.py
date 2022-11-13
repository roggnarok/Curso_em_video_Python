# Curso em vídeo - Desafio 046 - FOR
'''
    Faça um programa que mostre na tela uma contagem
    regressiva para o estouro de fogos de artifício,
    indo de 10 até 0, com uma pausa de 1 segundo
    entre eles.
'''
from time import sleep
print('Vai começar a contagem regressiva.')
for contador in range(10, 0, -1):
    print(f'{contador}')
    sleep(1)
print('Feliz Ano Novo!!!')
#This job was made by Rodrigo. https://github.com/roggnarok
