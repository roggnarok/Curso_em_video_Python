'''
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa irá custar R$ 7,00 por cada km acima do limite.
'''
velocidade = -1
while velocidade <=0 or velocidade > 200:
    velocidade = float(input('Qual é a velocidade do carro? '))

print(f'O carro está a {velocidade} km/h.')

if velocidade > 80.0:
    multa = float((velocidade - 80.0) * 7)
    print(f'PARE! Voce foi multado!\nO valor da multa é de R$ {multa}.')
else:
    print('Como a velocidade está abaixo de 80 km/h, siga em frente!')
#This job was made by Rodrigo. https://github.com/roggnarok
    
