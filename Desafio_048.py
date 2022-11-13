# Curso em vídeo - Desafio 048 - FOR
'''
    Faça um programa que calcule a soma entre todos os números ímpares 
    que são múltiplos de três(3) e que se encontram no intervalo de 1 até 500.
'''
soma = 0
for contador in range(1,501, 2): 
    if (contador % 3) == 0:    # Verifica se é divisível por 3 com resto 0.
        soma += contador       # Acumula em soma os números que satisfaz as condições.
print(f'A soma dos nº ímpares que são \
múltiplos de 3 é igual a {soma}.')
#This job was made by Rodrigo. https://github.com/roggnarok
