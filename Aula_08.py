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

#Desafios do nº 16 
#nº16 programa que lê um número real e mostra a sua parte inteira. 6.5321 --> 6
    #Ver as funções do módulo math
#nº17 programa recebe o valor co cateto oposto e do cateto adjacente e calcula a hipotenusa.
    #Ver as funções do módulo math
#nº18 O programa lê um ângulo qualquer e mostra valor do Seno, Cosseno e Tangente desse ângulo.
    #Ver as funções do módulo math
#nº19 Um professor que sortear um dos seus 4 alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

#nº20 Um professor quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos alunos e mostre a ordem sorteada.

#nº21 Faça um programa que abra e reproduza o áudio de um árquivo mp3.
