'''
Escreva um programa que leia DOIS valores inteiros e compare-os, mostrando na tela uma mensagem:
O primeiro valor é maior.
O segundo valor é maior.
Não existe valor maior, os dois são iguais.
'''
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
if n1 == n2:
    print('Não existe valor maior, os dois são iguais.')
elif n1 > n2:
    print('O primeiro valor é o maior.')
else:
    print('O segundo valor é o maior.')
#This job was made by Rodrigo. https://github.com/roggnarok