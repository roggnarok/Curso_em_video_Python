#027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nomeFatiado = input('Digite o nome completo: ').strip().split() #Armazena na variáre o nome já fatido e sem os espaços inicial e final

primeiroNome = nomeFatiado[0]
ultimoNome = nomeFatiado[-1]
print(f'O Primeiro nome é {primeiroNome}\
    \nO último nome é {ultimoNome}')
#This job was made by Rodrigo. https://github.com/roggnarok