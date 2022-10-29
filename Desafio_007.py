#Programa que recebe duas notas, calcula e mostra a média
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2)/2                       #Ordem de precedência entre operadores.
print(f'As notas foram {nota1} e {nota2}\
    \nA média é igual a {media :.2f}')