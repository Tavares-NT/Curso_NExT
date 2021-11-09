'''Faça um programa que recebe do usuário 10 valores de números inteiros, armazena em um vetor e apos percorre-lo exibe qual é o maior valor e a sua posição.'''

vetor = []
for i in range(1, 11):
  vetor.append(int(input("Digite um numero: ")))

print(max(vetor))
print(vetor.index(max(vetor)))