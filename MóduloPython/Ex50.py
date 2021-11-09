'''Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.'''

alunos = []
alturas = []

for i in range(10):
  alunos.append(input('Digite o nome do Aluno: '))
  alturas.append(float(input('Digite a altura do Aluno: ')))

idx = alturas.index(max(alturas))

print(f'O Aluno {alunos[idx]} é o mais alto, com {alturas[idx]}m de altura')

idx = alturas.index(min(alturas))

print(f'O Aluno {alunos[idx]} é o mais baixo, com {alturas[idx]}m de altura')