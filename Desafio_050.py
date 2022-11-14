# Curso em vídeo - Desafio 050 - FOR
'''
    Desenvolva um programa que leia seis números inteiros e mostre a soma
    apenas daqueles que forem pares. 
    Se o valor digitado for ímpar desconsidere-o.
'''
s = 0
for i in range(6):
    n = int(input(f'Digite o {i+1}º número: '))
    if (n % 2) == 0:
        s += n
print(f'\nA soma dos números pares\
 que foram digitados é {s}.')
#This job was made by Rodrigo. https://github.com/roggnarok
