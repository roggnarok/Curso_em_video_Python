'''
Escreva um programa que leia 3 números, mostre qual é o maior e qual é o menor.
'''
import math
n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
n3 = int(input('Digite o 3º número: '))

maior = max(n1, n2, n3) #Verifica e armazena quem é o maior
menor = min(n1, n2, n3) #Verifica e armazena quem é o menor
print(f'O maior número é {maior} e\no menor número é {menor}.')

#This job was made by Rodrigo. https://github.com/roggnarok