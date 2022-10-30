#Lé um número inteiro e mostra a sua tabuada
n = int(input('Digite um valor: '))
print(f'O valor digitado foi {n} e a tabuada do {n} é:\
    \n{n} x 1 = {n*1}\
    \n{n} x 2 = {n*2}\
    \n{n} x 3 = {n*3}\
    \n{n} x 4 = {n*4}\
    \n{n} x 5 = {n*5}\
    \n{n} x 6 = {n*6}\
    \n{n} x 7 = {n*7}\
    \n{n} x 8 = {n*8}\
    \n{n} x 9 = {n*9}\
    \n{n} x 10 = {n*10}')
    
#maneira de resolver o mesmo problema utilizando o FOR
print(f'Abaixo será apresentada a tabuada do {n}.')
for i in range(1,11):
    print(f'{n} x {i} = {n * i}')
#This job was made by Rodrigo. https://github.com/roggnarok
