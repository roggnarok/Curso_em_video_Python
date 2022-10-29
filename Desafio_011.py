#Usuário informa a largura e a altura de uma parede, o programa calcula a área e a quantidade em litros de tinta para pintá-la
largura = float(input('Informe a Largura da parede: '))
altura = float(input('Informe a Altura da parede: '))
area = largura * altura
rendimento = area / 2
print(f'A Largura da parede é de {largura} metros, a Altura é de {altura} metros\
    \nA área da parede é de {area} metros²\
    \nPara pintar essa parede, será necessário {rendimento :.2f} litros de tinta.')