'''Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.'''

import random
contador = [0,0,0,0,0,0]
temp = 0
for i in range(100):
  temp = random.randint(1,6)
  contador[temp-1] += 1
print(f'O dado lançado 100 vezes')
print(f'{contador[0]} vezes deu 1')
print(f'{contador[1]} vezes deu 2')
print(f'{contador[2]} vezes deu 3')
print(f'{contador[3]} vezes deu 4')
print(f'{contador[4]} vezes deu 5')
print(f'{contador[5]} vezes deu 6')