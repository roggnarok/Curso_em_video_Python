# Curso em vídeo - Desafio 051 - FOR
'''
    Desenvolva um programa que leia o primeiro
    termo e a razão de uma PA. No final, mostre
    os 10 primeiros termos dessa progressão. 
'''
n = 10                          # Define o contador, o número de vezes que o FOR será executado.
primeiro_termo = int(input(
'Digníssimo usuário, digite'
' o primeiro termo da Progressão: '
))
razao = int(input(
'Agora digite a razão dessa'
' mesma progressão: '))
print(f'Os {n} primeiros termos da P.A. são: ')
for i in range(n):
    print(f'{primeiro_termo}', end=' ')
    primeiro_termo += razao