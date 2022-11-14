# Curso em vídeo - Desafio 054 - FOR
'''
    Crie um programa que leia o ano de nascimento de 3 pessoas.
    No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''
import datetime
hoje = datetime.datetime.now()
anoAtual = hoje.year
maior = 0
menor = 0
ano = [] #Cria uma lista vazia
#For para receber e armazenar as 3 entradas de dados. APPEND
for i in range(3):
    ano.append(int(input('Digite o ano do seu nascimento: ')))

for contador in range(0, len(ano)):
    if (anoAtual - ano[contador]) >= 21: #Subtrai o (ano atual - ano digitado), se for maior ou igual a 21, então é maior de idade. 
        print(f'A pessoa que nasceu em {ano[contador]} é maior de idade.')
        maior += 1
    else:
        print(f'A pessoa que nasceu em {ano[contador]} é menor de idade.')
        menor += 1        
print(f'O número de maiores de idade é {maior}.\
    \nO número de menores de idade é {menor}.')
#This job was made by Rodrigo. https://github.com/roggnarok