#027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = input('Digite o nome completo: ')
nome = nome.strip() #Remove os espaços no começo e final
fatiado = nome.split()
ultimoNome = fatiado[-1]
print(f'The last name is {ultimoNome}')
#This job was made by Rodrigo. https://github.com/roggnarok