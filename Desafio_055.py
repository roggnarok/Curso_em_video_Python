# Curso em vídeo - Desafio 055 - FOR
'''
    Faça um programa que leia o peso de 5 pessoas. No final, mostre qual 
    foi o maior e o menor peso lidos. 
'''
peso = [] #Cria uma lista vazia
for i in range(5):
    peso.append(int(input(f'Digite o peso da pessoa {i+1}: ')))
print(f'O maior peso digitado foi {max(peso)}.\
    \nO menor peso digitado foi {min(peso)}.')
#This job was made by Rodrigo. https://github.com/roggnarok
