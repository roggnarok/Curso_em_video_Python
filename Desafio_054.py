# Curso em vídeo - Desafio 054 - FOR
'''
    Crie um programa que leia o ano de
    nascimento de sete pessoas. No final,
    mostre quantas pessoas ainda não
    atingiram a maioridade e quantas já
    são maiores.
'''
import datetime
hoje = datetime.datetime.now()
ano_atual = hoje.year
maior = 0
menor = 0
for i in range(7):
    ano = int(input('Digite o ano do seu nascimento: '))
    if (ano_atual - ano) >= 18:
        maior += 1
    else:
        menor += 1
print(
f'O número de maiores de idade é {maior}.\n'
f'O número de menores de idade é {menor}.'
)