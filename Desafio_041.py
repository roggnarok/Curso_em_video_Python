'''
A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre a sua categoria, de acordo com a idade:
até 9 anos: MIRIM
até 14 anos: INFANTIL
até 19 anos: JUNIOR
até 20 anos: SÊNIOR
Acima: MASTER
'''
from datetime import date
nascimento = int(input('Digite o ano de nascimento do atleta: '))
idade = date.today().year - nascimento #date.today().year --> utiliza somente o ano 

if idade <= 9:
    print(f'O atleta possui {idade} anos e está na categoria MIRIM.')
elif idade <= 14:
    print(f'O atleta possui {idade} anos e está na categoria INFANTIL.')
elif idade <= 19:
    print(f'O atleta possui {idade} anos e está na categoria JUNIOR.')
elif idade <= 20:
    print(f'O atleta possui {idade} anos e está na categoria SÊNIOR.')
else:
    print(f'O atleta possui {idade} anos e está na categoria MASTER.'),