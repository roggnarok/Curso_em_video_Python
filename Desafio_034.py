'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$ 1.250,00 calcule aumento de 10%
Para os inferiores ou iguais, o aumento é de 15%
'''
salario = float(input('Qual é o salário do funcionário? '))
if salario > 1250:
    print(f'O novo salário corrigido em 10% é R${(salario * 1.10):.2f}')
else:
    print(f'O novo salário corrigido em 15% é R${(salario * 1.15):.2f}')
#This job was made by Rodrigo. https://github.com/roggnarok