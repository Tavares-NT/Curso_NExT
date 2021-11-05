'''Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.'''

C = float(input("Digite a temperatura em Celsius: "))
F = (C * 1.8) + 32
print(f"A temperatura em Fahrenheit é: {round(F, 1)}º")