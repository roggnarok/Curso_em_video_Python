# Curso em vídeo - Desafio 050 - FOR
'''
    Desenvolva um programa que leia seis
    números inteiros e mostre a soma
    apenas daqueles que forem pares.
    Se o valor digitado for ímpar desconsidere-o.
'''
s = 0
for i in range(6):
    n = int(input('Prezado usuário, digite um número: '))
    if (n % 2) == 0:
        s += n
print(
'\nA soma dos números pares'
f' que foram digitados é {s}.'
)