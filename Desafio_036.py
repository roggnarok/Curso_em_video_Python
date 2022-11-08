'''
Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. O programa vai perguntar o VALOR DA CASA, o SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar.

Calcule o valor da presstação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado. 
'''
valorDaCasa = float(input('Qual é o valor do imóvel? '))
salario = float(input('Qual é a sua renda (salário)? '))
prazoAno = int(input('Em quantos anos você quer pagar? '))

meses = 12 * prazoAno
prestacao = valorDaCasa / meses
trintaPorCentoSalario = salario * 0.30

if prestacao > trintaPorCentoSalario:
    print(f'Você não vai poder comprar essa casa \033[31m:(\033[m\
        \nA prestação ({prestacao:.2f}) é maior do que 30% do seu salário ({trintaPorCentoSalario:.2f}).')
else:
    print(f'Você vai poder comprar essas casa!\
        \nA prestação mensal será de R$ {prestacao:.2f}\
        \nO financiamento será feito em {meses} meses.')
#This job was made by Rodrigo. https://github.com/roggnarok