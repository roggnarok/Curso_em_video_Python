'''
Faça um programa que leia o ano de nascimento de uma pessoa e informe, de acordo com sua idade.
-Se ele ainda vai se alistar
-Se é a hora deçe se alsitar
-Se já passou do tempo do alistamento
O programa também deverá mostrar o tempo em anos que falta ou que passou para ele se alistar;
'''
from datetime import date
#verificação de que o usuário irá digitar apenas F ou M
sexo = 'a'
while (sexo != "F") and (sexo != "M"):
    sexo = input('Digite o seu sexo (M/F):').upper()

#Se o sexo for == a M, então:
if sexo == "M":
    nascimento = int(input('Digite seu ano de nascimento: ')) #pergunta o ano de nascimento
    idade = date.today().year - nascimento #date.today().year --> utiliza somente o ano 
    if idade > 18: #Se a idade for maior que 18
        print(f'Olá, o tempo do alistamento já passou.\
        \nVocê tem {idade} anos e deveria ter se alistado há {(idade-18)} anos atrás.')
    elif idade == 18: #Se a idade for igual a 18
        print(f'Olá, você tem {idade} anos e está na idade de se alistar.')
    else: #Senão:
        print(f'Olá, o tempo do alistamento está chegando.\
        \nVocê tem {idade} anos e devdeverá se alistar em {(18-idade)} anos.')
else: #Senão: (Se o sexo não for igual a M)
    print('Como o seu sexo não é masculino, você não precisa se alistar no serviço militar.')
#This job was made by Rodrigo. https://github.com/roggnarok