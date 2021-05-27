# Desafio 100 - FUNÇÕES
''' Faça um programa que tenha uma lista chamada números e duas funções
    chamadas sorteio() e somaPar(). A primeira função vai sortear 5 números
    e vai colocá-los dentro da lista e a segunda função vai mostrar a soma
    entre todos os valores PARES sorteados pela função anterior.'''

import random
def sorteio(lista):             # Cria a função sorteio que recebe uma lista
    for value in range(0,5):        # Loop acontecerá 5 vezes (0, 1, 2, 3, 4)
        n = random.randint(0,10)        # n recebe um valor aleatório entre 0 e 19
        lista.append(n)                 #O valor n é adicionado no final da lista
    print(f'A lista com 5 valores sorteados é {lista}.')


def somaPar(lista):             # Cria a função somaPar que recebe uma lista
    s = 0                           # o valor zero é atribuído à variável s
    for value in lista:             # Loop ocorrerá na lista
        if (value % 2) == 0:            # Se o valor da lista for PAR, entáo faça:
            s = s + value                   # s recebe a soma de s com valor.
    print(f'A soma dos valores PARES da lista é igual a {s}.')


# Programa Principal
numeros = list()    # números recebe uma lista vazia.
sorteio(numeros)    # a função sorteio envia 'números' como parâmetro.
somaPar(numeros)    # a função somaPar envia os 'números' como parâmetro.