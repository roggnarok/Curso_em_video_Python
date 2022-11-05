'''
Escreva um programa que leia o comprimento de 3 segmentos de reta e informe se é possível ou não fechar um triângulo.
'''
#Criei uma função que calcula o módulo de dois valores.
def modulo (x, y):
    mod = x - y
    if mod < 0:
        mod *= -1  
    return mod
#Recebe os valores do usuário
a = float(input('Digite o tamanho do segmento a: '))
b = float(input('Digite o tamanho do segmento b: '))
c = float(input('Digite o tamanho do segmento c: '))

#Calcula os módulos
modAB = modulo(a,b)
modAC = modulo(a,c)
modBC = modulo(b,c)

#verifica a condição para ser um triangulo
'''
REGRA: Um de seus lados deve ser maior que o valor absoluto (módulo) da diferença dos outros dois lados e menor que a soma dos outros dois lados.
|A-B| < c < (A+B)
'''
if (c> modAB and c < (a+b)) and (b> modAC and b < (a+c)) and (a> modBC and a < (b+c)):
    print('É um triangulo')
else:
    print('Não é um triangulo')
#This job was made by Rodrigo. https://github.com/roggnarok

