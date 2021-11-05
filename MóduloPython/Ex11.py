'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    1) o produto do dobro do primeiro com metade do segundo.
    2) soma do triplo do primeiro com o terceiro.
    3) terceiro elevado ao cubo.'''

num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))
num3 = float(input("Agora digite um número real: "))

a = (num1 * 2) * (num2 / 2)
b = (num1 * 3) + (num3)
c = num3 ** 3

print("1)", a, "\n2)", b, "\n3)", round(c, 1))