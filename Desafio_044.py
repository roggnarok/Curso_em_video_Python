'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu PREÇO NORMAL e CONDIÇÃO DE PAGAMENTO:
- À vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- em até 2x no cartão: Preço normal
- em 3x ou mais no cartão: 20% de juros
    perguntar a quantidade de parcelas e calcular o valor
'''
valorPrd = float(input('Qual é o valor do produto: '))
formaDePagto = int(input('Qual será a forma de pagamento?\
    \n[1] - À vista (dinheiro ou cheque).\
    \n[2] - À vista no cartão.\
    \n[3] - 2x no cartão.\
    \n[4] - 3x ou mais no cartão.\
    \nOpção: '))

if formaDePagto == 1:
    print(f'Você obteve 10% de desconto e irá pagar R${(valorPrd*0.9):.2f}')
elif formaDePagto == 2:
    print(f'Você obteve 5% de desconto e irá pagar R${(valorPrd*0.95):.2f}')
elif formaDePagto == 3:
    print(f'Você escolheu parcelar em 2x, não terá acréscimo nem desconto.\
        \n Você irá pagar 2x de R${(valorPrd/2):.2f}')
elif formaDePagto == 4:
    parcelas = int(input('Você escolheu pagar em 3x ou mais.\
        \nEm quantas vezes quer parcelar? '))
    print(f'Você escolheu parcelar em {parcelas}x, terá acréscimo de 20%.\
        \nVocê irá pagar R${valorPrd*1.2} em {parcelas}x de R${((valorPrd*1.2)/parcelas):.2f}')
