# Curso em vídeo - Desafio 053 - FOR
'''
    Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
    desconsiderando os espaços.
    APOS A SOPA -- A SACADA DA CASA
    A TORRE DA DERROTA -- O LOBO AMA O BOLO
'''
# Recebe a frase, elimina os espaços no começo e fim, converte em maiúscula.
frase = input('Digite a frase: ').strip().upper()
# FAz o fatiamento das strings da frase e armazena em palavras.
palavras = frase.split()
# Concatena as palavas usando um espaço vazio entre elas ''.
junto = ''.join(palavras)
# Cria uma variável vazia chamada inverso
inverso = ''
# Mostra o que foi feito anteriormente como parte do entendimento. 
# Não faz parte do programa oficial, está aí para aprendizagem.
print(
f'A Frase {frase}\n'
f'A Palavra {palavras}\n'
f'Elas Juntas {junto}\n'
f'O LEN(tamanho) de Junto é {len(junto)}'
)
'''
O range começa na ultima posição do Len -1 e
Vai até o índice zero[0] , por isso o segundo parâmetro é -1
O passo do Range é -1, pois é decrescente. 
'''
for i in range(len(junto) -1, -1, -1):
    inverso += junto[i]
# Mostra o resultado da inversão da string.
print(f'O inverso de {junto} é {inverso}.')
# se a str em inverso for igual a str em junto, temos um palíndromo. 
if inverso == junto:
    print(f'Temos um Palíndromo!!')
else:
    print(f'Não temos um Palíndromo.')
#This job was made by Rodrigo. https://github.com/roggnarok
