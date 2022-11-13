'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule o IMC e mostre seu status, de acordo com a tabela abaixo:
Abaixo de 18.5 (abaixo do peso)
Entre 18.5 e 25 (Peso Ideal)
Entre 25 e 30 (Sobrepeso)
Entre 30 e 40 (Obseidade)
Acima de 40 (Obesidade mórbida)
'''
peso = float(input('Digite o seu peso em Kg: '))
altura = float(input('Digite a sua alura em metros: '))
imc = round(peso / (altura ** 2), 1)

print(f'\nSua altura é {altura}m\nSeu peso é {peso}Kg\nSeu IMC é {imc}.\n')

if imc < 18.5:
    print('Você está \033[31mAbaixo do peso\033[m')
elif imc < 25:
    print('Você está no \033[31mPeso ideal\033[m')
elif imc < 30:
    print('Você está com \033[31mSobrepeso\033[m')
elif imc < 40:
    print('Você está \033[31mObeso\033[m')
else:
    print('Você está com \033[31mObesidade mórbida\033[m')
#This job was made by Rodrigo. https://github.com/roggnarok
