'''Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.'''

numeros = []
x = 0
while x < 5:
  numeros.append(int(input('Digite um numero: ')))
  x += 1

multiplica = 1
soma = 0

for n in numeros:
  multiplica *= n
  soma += n

print(soma)
print(multiplica)
print(numeros)