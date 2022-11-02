#026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = input('Digite a Frase: ')
frase = frase.strip() #Remove os espaços em no começo e final da frase
frase = frase.lower() #Converte a frase para minúsculo
numeroDeA = frase.count('a') #Conta quantas vezes a letra "a" aparece na frase
primeiroA = frase.find('a') #Mostra a posição da 1ª aparição da letra "a"
ultimoA = frase.rfind('a') #Mostra a posição da ultima aparição da letra "a"
print(f'Na frase digitada, a letra "a" aparece {numeroDeA} vezes.\
    \nEla aparece a primeira vez na posição {primeiroA}\
    \nEla aparece na última vez na posição {ultimoA}.')
#This job was made by Rodrigo. https://github.com/roggnarok