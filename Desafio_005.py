#Receba um número, converta em inteiro, mostre o sucessor e o antecessor do número digitado.
a = int(input('Digite um valor: '))
anterior = a-1
sucessor = a+1
print(f'O número digitado foi {a}\
    \no sucessor dele é {sucessor}\
    \no antecessor dele é {anterior}')