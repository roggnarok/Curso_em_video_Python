#nº17 programa recebe o valor do cateto oposto e do cateto adjacente e calcula a hipotenusa.
    #Ver as funções do módulo math
import math
from math import hypot # --> Da biblioteca math impota a função hypot
catetoAdjacente = float(input('Digite o valor do Cateto Adjacente: '))
catetoOposto = float(input('Digite o valor do Cateto Oposto: '))
hipotenusa = math.hypot(catetoAdjacente, catetoOposto) #Cálculo da hipotenusa usando a função HYPOT
print(f'O valor da hipotenusa é {hipotenusa}')
#This job was made by Rodrigo. https://github.com/roggnarok
