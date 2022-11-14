# Curso em vídeo - Desafio 049 - FOR
'''
    Refaça o Desafio 009, mostrando a tabuada de um número que o usuário
    escolher, só que agora utilizando um só laço FOR.
'''
n = int(input('Prezado usuário, digite um número de sua preferência: '))
print(f'Abaixo será apresentada a tabuada do {n}.')
for i in range(1,11):
    print(f'{n} x {i} = {n * i}')
#This job was made by Rodrigo. https://github.com/roggnarok
