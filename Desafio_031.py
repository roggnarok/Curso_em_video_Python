'''
Escreva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200 Km e
R$ 0,45 / Km para viagens mais longas.
'''
distanciaViagem = int(input('Qual é a distância da viagem em Km? '))

if distanciaViagem <= 200:
    print(f'O preço da passagem é de R$ {(distanciaViagem * 0.50):.2f}.')
else:
    print(f'O preço da passagem é de R$ {(distanciaViagem * 0.45):.2f}.')
#This job was made by Rodrigo. https://github.com/roggnarok