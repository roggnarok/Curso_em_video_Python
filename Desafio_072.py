# Desafio72 Tupla - 43 minutos - https://www.youtube.com/watch?v=0LB3FSfjvao&t=2718s
numeros = (
    'Zero',
    'Um',
    'Dois',
    'Três',
    "Quatro",
    "Cinco",
    "Seis",
    "Sete",
    "Oito",
    "Nove",
    "Dez",
    "Onze",
    "Doze",
    "Treze",
    "Quatorze",
    "Quinze",
    "Dezesseis",
    "Dezessete",
    "Dezoito",
    "Dezenove",
    "Vinte",
)
a = int(input("Digite o seu número entre 0 e 20: "))
while a < 0 or a > 20:
    print("Pãããã!\tNúmero errado.")
    a = int(input("Digite o seu número entre 0 e 20: "))
while a >= 0 and a <= 20:
    print(numeros[a])
    break
print(quebra)