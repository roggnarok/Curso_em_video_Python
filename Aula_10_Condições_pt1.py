
#Exercício de 28 a 35
'''
Algorítimo para um carro chegar em determinado ponto:
carro.siga()
carro.esquerda()
carro.siga()
carro.direita()
carro.siga()
carro.direita()
carro.siga()

Duas opções de caminho:
carro.siga()
se carro.esquerda()
    Esquerda:
    carro.esquerda()
    carro.siga()
    carro.direita()
    carro.siga()
    carro.direita()
    carro.esquerda()
    carro.siga()
    carro.direita()
senão:
    Direita:
    carro.direita()
    carro.siga()
    carro.esquerda()
    carro.siga()
carro.pare()

#CONDIÇÃO
if carro.esquerda():
    bloco True
else:
    bloco False

#Exemplo1
tempo = int(input('Quantos anos tem seu carro?'))
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')
print('===FIM===')
#Exemplo2 Mesma situação do exemplo acima:
tempo = int(input('Quantos anos tem seu carro?'))
print('Carro novo' if tempo <= 3 else 'Carro velho') #Condicional IF toda em uma linha e dentro do PRINT

#Exemplo3
nome = str(input('Qual é o seu nome? '))
if nome == 'Rodrigo':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é bem normal!')
print(f'Bom dia {nome}!')
'''
#Exemplo4
n1 = float(input('Digite a 1ª nota: '))
n2 = float(input('Digite a 2ª nota: '))
m = (n1 + n2) / 2
print(f'Sua nota final foi {m}')
if m >= 6.0:
    print('Aprovado')
else:
    print('Reprovado')

