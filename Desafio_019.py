# um professor quer sortear um dos seus quatro alunos para apagar o quadro. O programa deve ler o nome deles, sortear um aluno e mostrar na tela.
from random import sample
aluno1 = str(input('Digite seu o nome do 1º aluno: '))
aluno2 = str(input('Digite seu o nome do 2º aluno: '))
aluno3 = str(input('Digite seu o nome do 3º aluno: '))
aluno4 = str(input('Digite seu o nome do 4º aluno: '))
alunosLista = [aluno1, aluno2, aluno3, aluno4] #Criação de uma lista com os alunos
selecionado = sample(alunosLista, k=1) #Sample faz uma seleção aleatória de elementos(k) dentro de uma lista, por isso os alunos estão entre [] Colchetes, e o valor de k=1 (pois quero que apenas 1 elemento da lista seja selecionado)
print(f'O aluno selecionado foi {selecionado}')
#This job was made by Rodrigo. https://github.com/roggnarok