# Curso em vídeo - Desafio 055 - FOR
'''
    Faça um programa que leia o peso de
    cinco pessoas. No final, mostre qual 
    foi o maior e o menor peso lidos. 
'''
peso = []
for i in range(5):
    valor = int(input(f'Digite o peso da pessoa {i+1}: '))
    peso.append(valor)
print(
f'O maior peso digitado foi {max(peso)}.\n'
f'O menor peso digitado foi {min(peso)}.'
)