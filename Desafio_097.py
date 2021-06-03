# Desafio 097
''' Faça um programa que tenha uma função chamada escreva(), que recebe
    um texto qualquer como parâmetro e mostre uma mensagem com tamanho
    das linhas superior e inferior adaptavél.'''

def escreva(str):
    linha = ('~' * len(str))
    print(linha)
    print(str)
    print(linha)


# Programa principal
texto = input("Escreva algo: ")
escreva(texto)