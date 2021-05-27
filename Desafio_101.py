# Desafio 101 - FUNÇÕES
'''
    Crie um programa que tenha uma função chamada voto() que vai Receber
    o ano de nascimento de uma pessoa, retornando um valor literal
    indicando se a pessoa tem voto Obrigatório, Facultativo ou não vota.
'''
def voto(ano):
    from datetime import date
    a = date.today().year
    idade = a - ano
    if idade < 16:
        return 'Não vota!'
    elif (idade >= 16 and idade < 18) or idade >= 65:
        return 'Voto Facultativo!'
    else:
        return 'Voto Obrigatório!'


# Programa Principal
ano = int(input('Em que ano você nasceu? '))
print(voto(ano))