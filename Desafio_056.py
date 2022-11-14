# Curso em vídeo - Desafio 056 - FOR
'''
    Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
    No final do programa mostre, A média de idade do grupo,
    Qual o nome do homem mais velho, Quantas mulheres têm menos de 20 anos.
'''
idade = []
nome = []
sexo = []
media = 0
somaIdade = 0
maiorIdadeHomem = 0 
nomeHomemVelho = []
#FOR para receber os dados e armazenar nas variáveis
for i in range(4):
    nome.append(input('Digite o nome: '))
    idade.append(int(input('Digite a idade: ')))
    sexo.append(input('Digite o sexo [M/F]: ').strip().upper())

#FOR para o laço de verificação se existe homem e qual é o mais velho.
for i in range(0, len(sexo)):
    if i == 0 and sexo[i] in 'Mn':
        maiorIdadeHomem = idade[i]
        nomeHomemVelho = nome[i]
    if sexo[i] in 'Mn' and idade[i] > maiorIdadeHomem:
        maiorIdadeHomem = idade[i]
        nomeHomemVelho = nome[i]

#PRINT IF --> se houber homem, senão:       
if nomeHomemVelho != []: #Se a lista não estiver vazia, mostre:
    print(f'O nome do homem mais velho é {nomeHomemVelho} e a idade dele é {maiorIdadeHomem} anos.')
else:
    print('Não existe homem neste grupo.')

#Cálculo da soma das idades digitadas.
for contador in range(0, len(idade)):
    somaIdade += idade[contador]
media = somaIdade / len(idade) #Cálculo da média de idade do grupo
print(f'A média de idade do grupo é {(media):.0f} anos.')

#Verifica se o Sexo é F e se a idade é < 20, se sim:
contadorMulher = 0
for c in range(0, len(sexo)):
    if (sexo[c] == 'F') and (idade[c] < 20):
        contadorMulher += 1

#PRINT IF --> Mostra a qtd de mulher menor de 20 anos, ou não mostra se não houver.
if contadorMulher <= 0:
    print('Não existe mulher menor de 20 anos.')
else:
    print(f'Existe(m) {contadorMulher} mulher(es) menor(es) de 20 anos.')
#This job was made by Rodrigo. https://github.com/roggnarok
