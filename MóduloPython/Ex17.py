'''Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.'''

import math
area = float(input("Informe o tamanho da área a ser pintada: "))
qtdLitros = area / 6
qtdLatas = math.ceil(qtdLitros / 18)
qtdGalao = math.ceil(qtdLitros / 3.6)
valorLata = qtdLatas * 80.00
valorGalao = qtdGalao * 25.00

litrosComFolga = qtdLitros + (qtdLitros * 0.10)
valorMisto = ((litrosComFolga // 18) * 80.00 + (math.ceil(((litrosComFolga % 18) / 3.6) * 25)))

print(f"Quantidade de latas de 18 litros necessárias: {qtdLatas}")
print(f"Valor a pagar: R${valorLata}")
print(f"Quantidade de latas de 3.6 litros necessárias: {qtdGalao}")
print(f"Valor a pagar: R${valorGalao}")
print(f"Valor a pagar misturando dois tipos: R${math.ceil(valorMisto)}")