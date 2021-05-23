# Curso em vídeo - Desafio 052 - FOR
'''
    Faça um programa que leia um número inteiro e
    diga se ele é ou não um número primo.
'''
c = 0
num = int(input('Digite um número: '))
if num <= 1:
    print(f'O número {num} não é primo.')
else:
    for i in range(1, num+1):
        if (num % i) == 0:
            c += 1
    if (c == 2):
        print(f'O número {num} é primo!')
    else:
        print(f'O número {num} não primo!')
