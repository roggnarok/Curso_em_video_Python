# Desafio73 - 45 minutos - https://www.youtube.com/watch?v=0LB3FSfjvao&t=2718s
'''Programa que a partir de uma tabela, mostra 1)Os 5 primeiros,
    2)Os 4 últimos, 3)A lista em ordem alfabética e 4)'''
times = (
    "Corinthians",
    "Santos",
    "Chapecoense",
    "Sport Recife",
    "Paysandú",
    "Botafogo",
    "Grêmio",
    "Goiás",
    "Novohorizontino",
    "Barcelona",
    "Chelsea",
    "Boca Juniors",
)
print("Os 5 primeiros colocados são.")
# 1.Mostra os 5 primeiros colocados
for i in range(5):  # Loop no For será repetido 5 vezes.
    print(
        f'Em {i+1}º lugar está o time do {times[i]}'
    )  # Imprime o valor contido no índice dentro da Tupla chamada times.
# 2.Mostra os 4 últimos colocados
print(quebra)
print('Os 4 últimos são:')
i = 8  # Atribui 8 à variável i.
while i <= 11:  # Enquanto i for menor ou igual a 11:
    print(times[i])  # Mostra o time que se encontra na posição i da Tupla.
    i += 1  # Acrescenta 1 ao valor que está em i.
# 3.Mostra a lista em ordem alfabética.
print(quebra)
print("Os times em ordem alfabética são:\n", sorted(times))
# 4.Mostra a posição de determinado time no campeonato.
print(quebra)
clube = input("Digite o time: ")
if clube in times:
    print(f'O time da {clube} está na', (times.index(clube) + 1), 'ª posição.')
else:
    print(
        "O time pesquisado não está no campeonato, pode ser que esteja na 2ª ou 3ª divisão."
    )
    pass