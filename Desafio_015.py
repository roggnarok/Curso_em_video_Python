#Calcula o valor a ser pago pelo aluguel de um carro
#R$ 60 por dia de aluguel + R$ 0,15 por Quilometro rodado.
dias = int(input('Informe a quandidade de dias que o carro esteve alugado: '))
km = float(input('Informe a quantidade de Quilometros rodados: '))
valorDoAluguel = (dias * 60)+(km * 0.15)
print(f'O valor a ser pago é de R$ {valorDoAluguel:.2f}')
