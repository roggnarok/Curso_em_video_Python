'''
Escreva um programa que leia duas notas de um aluno e calcule sua média simples.
No final mostre uma mensagem de acordo com a média tingida. 
- Média abaixo de 5.0: REPROVADO
- Média entre de 5.0 e 6.9: RECUPERAÇÃO
    Se em recuperação, solicitar a nota da recuperação, calcular uma nova média e mostrar se Aprovado (>= 7) ou Reprovado
- Média abaixo de 7.0: APROVADO
'''
nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))
media = round((nota1 + nota2)/2, 1) #round(valor,1) Arredonda o valor p/ 1 casa decimal

if media < 5:
    print(f'Sua média foi {media} e você está REPROVADO')
elif 5 <= media <= 6.9:
    print(f'Sua média foi {media} e você está de RECUPERAÇÃO')
    notaRecup = float(input('Digite a nota da recuperação: '))
    media = round((media + notaRecup) / 2, 1)
    if media < 7:
        print(f'Sua média após a recuperação foi {media} e você está REPROVADO')
    else:
        print(f'Sua média após a recuperação foi {media} e você está APROVADO')
elif media >= 7.0:
    print(f'Sua média foi {media} e você está APROVADO')
#This job was made by Rodrigo. https://github.com/roggnarok
