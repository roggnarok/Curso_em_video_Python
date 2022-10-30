#Bibliotecas em python
import math #Importa toda a biblioteca math
from math import pow, sqrt #Da Biblioteca math, importa somente o pow e o sqrt

valor = float(input('Digite um valor para calcular a raiz: '))
raiz = math.sqrt(valor)                     #Utilizar o . (ponto) para acessar a função sqrt
print(f'A raíz de {valor} é {raiz:.3f}')

print(f'Imprime o valor de Pi {math.pi}') #Importei o valor de Pi da biblioteca Math

import random #Importa toda a biblioteca Random
numAleatorio = random.random()      #Gera número aleatório entre 0 e 1
print(f'O número aleatório gerado foi {numAleatorio}\
    Esse mesmo número com 3 casas decimais {numAleatorio:.3f}')
numAleatorioInt = random.randint(1,13) #Gera um num aleatório INTEIRO entre 1 e 13
print(f'O número aleatório inteiro gerado foi o {numAleatorioInt}')
