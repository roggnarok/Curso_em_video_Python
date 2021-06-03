# Desafio 099
''' Faça um programa que tenha uma função chamada maior(), que receba vários
    parâmetros com valores inteiros. O programa tem que analisar todos os
    valores e dizer qual é o maior.'''
def maior(*numeros):
    n = max(numeros)
    print(f'De toda a lista {numeros} o maior valor é {n}.')


# Programa Principal
maior(2, 3, 5, 6, 9, 4, 62, 0, 12)