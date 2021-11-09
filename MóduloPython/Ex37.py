'''Faça um programa que leia 5 números e informe o maior número.'''

num = []
for i in range(0,5):
  num.append(int(input("Insira um número: ")))
print(max(num))