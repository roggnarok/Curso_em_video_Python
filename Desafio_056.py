# Curso em vídeo - Desafio 056 - FOR
'''
    Desenvolva um programa que leia o 
    nome, idade e sexo de 4 pessoas. 
    No final do programa mostre, A média de idade do grupo,
    Qual o nome do homem mais velho, Quantas mulheres têm 
    menos de 20 anos. 
'''
idade = []
nome = []
for i in range(4):
    nome.append(input('Digite o nome: '))
    idade.append(int(input('Digite a idade: ')))
    
