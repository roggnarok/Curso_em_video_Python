#nº16 programa que lê um número real e mostra a sua parte inteira. 6.5321 --> 6
    #math.trunc(x) --> retorna a parte inteira do número
import math
from math import trunc #Importa somente a função trunc da biblioteca math
numero = float(input('Digite um número real: '))
print(f'A parte inteira do número digitado é {math.trunc(numero)}')
#This job was made by Rodrigo. https://github.com/roggnarok
