'''
Escreva um programa que leia um ano e mostre se ele é BISSEXTO.
Dica: Qualquer ano que seja uniformemente divisível por 4, 100 e 400 é um ano bissexto
'''
ano = int(input('Digite o ano: '))
print(ano % 4)
print(ano % 100)
print(ano % 400)
bissexto = (((ano % 4) == 0) and ((ano % 100) != 0) or ((ano % 400) == 0))
 #Se o resto da divisão do ano por 4 for igual a zero e o resto da divisão por 100 for diferente de zero, ou o resto da divisão por 400 for igual a zero, o ano é bissexto
if bissexto == True:
    print(f'O ano {ano} é BISSEXTO!')
else:
    print(f'O ano {ano} não é bissexto!')
#This job was made by Rodrigo. https://github.com/roggnarok