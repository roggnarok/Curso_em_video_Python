# Curso em vídeo - Desafio 052 - FOR
'''
    Faça um programa que leia um número inteiro
    e diga se ele é ou não um número primo.
'''
while True:
    num = int(input('Forneça um valor para este programa: '))
    if num <= 1:
        print(f'O número {num} não é primo.')
    for i in range(2, num, 1):
        if (num % i) == 0:
            print(f'O número {num} não é primo.')
            break
        else:
            print(f'O número {num} é primo!')
            break

