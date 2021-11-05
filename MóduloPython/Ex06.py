'''Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.'''

pi = 3.14
r = float(input("Digite o raio do círculo: "))
A = pi * (r ** 2)
print(f"A área do círculo é: {round(A, 2)}cm²")