'''Crie um programa que tenha uma função que receba uma lista de números inteiros e exiba todos os valores multiplicados por um valor inserido pelo usuário.'''

def multiplica():
  lista = [1,2,3,4,5,6,7,8,9,10]
  for i in range(0,10):
    print(f"{n} * {lista[i]} = {n*lista[i]}")
n = int(input("Digite um número: "))
multiplica()