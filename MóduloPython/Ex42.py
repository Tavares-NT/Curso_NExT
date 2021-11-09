'''Faça um programa que recebe um número de 1 a 10 do usuário e imprime a tabuada de multiplicação desse número'''

n = int(input("digite um numero entre 1 e 10: "))

print(f"Tabuada de {n}")
for i in range(1, 11):
  print(f"{n} * {i} = {n*i}")