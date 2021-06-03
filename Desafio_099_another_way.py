# Desafio 099- Um jeito modificado por mim;
''' Resolução do exercício 099 de outra forma.
    Dessa forma abaixo, o tamanho da lista é aleatório entre 0 e 10.
    Após isso, os valores a serem incluídos na lista são definidos
        também de forma de aleatória.
    É uma lista de tamanho aleatório(0,10) com valores aleatórios(0,100)
    Esses números serão passados para  a função maior e a função '''

import random

def maior(num=list):
    maior = max(num)
    print(
    f'Os valores informados para '
    f'a função foram: {num}\n'
    f'O maior valor da lista é {maior}.'
    )

'''Define o tamanho da lista
aleatóriamente com valores entre 0 e 9'''
tamanho = (random.randint(0,10))
print(f'{tamanho} será o tamanho da lista.')

# Cria uma lista vazia de nome num.
num = list()

# Imprime o tamanho da lista incialmente.
print(f'Tamanho inicial da lista é {len(num)}')

# Imprime o tipo da variável num.
print(f'O tipo da lista é {type(num)}')

# Cria a lista com números aleatórios entre 0 e 99.
for value in range(tamanho):
    num.append(random.randint(0,100))

# Mostra a lista que foi criada.
print(
f'A lista criada foi {num}\n'
f'\to tipo é {type(num)}\n'
f'\to tamanho da lista é {len(num)}.'
)

# Chama a função maior e envia como parâmetro a lista criada.
maior(num)