# Desafio 096
''' Faça um programa que tenha uma função chamada área(),
    que receba as dimensões de um terreno retangular(largura e comprimento)
    e mostre a área do terreno.'''

def area(x,y):
    area = x * y
    print(f'A área de um terreno {x}x{y} é: {area:.2f}m².')


# Programa principal
largura = float(input("Largura: "))
comprimento = float(input("Comprimento: "))
area(largura, comprimento)