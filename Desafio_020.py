# um professor quer sortear a ordem de apresentação de trabalhos dos alunos. O programa deve ler o nome deles, sortear essa ordem de apresentação e mostrar na tela.
from random import sample
aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Terceiro aluno: '))
aluno4 = str(input('Quarto aluno: '))
alunosLista = [aluno1, aluno2, aluno3, aluno4] #Criação de uma lista com os alunos
apresentacao = sample(alunosLista, k=4) #Sample faz uma SELEÇÃO ALEATÓRIA de elementos(k) dentro de uma lista, o valor de k=4 (pois quero que 4 elementos da lista sejam selecionados)
print(f'A ordem de apresentação será {apresentacao}')
#This job was made by Rodrigo. https://github.com/roggnarok