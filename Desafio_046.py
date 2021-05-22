# Curso em vídeo - Desafio 046 - FOR
'''
    Faça um programa que mostre na tela uma contagem
    regressiva para o estoudo de fogos de artifício,
    indo de 10 até 0, com uma pausa de 1 segundo
    entre eles.
'''
from time import sleep
print(f'Vai começar a contagem regressiva...')
for i in range(10, 0, -1):
    print(f'{i}', end=" ")
    sleep(0.333)
    for c in range(0,3):
        print('.', end=" ")
        sleep(0.333)
print('Feliz Ano Novo!!!')
