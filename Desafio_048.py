# Curso em vídeo - Desafio 048 - FOR
'''
    Faça um programa que calcule a soma
    entre todos os números ímpares que
    são múltiplos de três(3) e que se
    encontram no intervalo de 1 até 500.
'''
soma = 0
for i in range(1,501):
    if (i % 2) != 0:        # Verifica se não é par.
        if (i % 3) == 0:    # Verifica se é divisível por 3 com resto 0.
            soma += i       # Recebe o valor da soma dos números que satisfazem as condições. 
print(
'A soma dos ímpares que são'
f' múltiplos de 3 é igual a {soma}.'
)