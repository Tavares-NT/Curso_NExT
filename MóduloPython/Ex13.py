'''Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7'''

sexo = input("Qual o seu sexo (M / F)? ")
sexo = sexo.upper()
h = float(input("Informe a sua altura: "))

if sexo == "M":
  pesoIdeal = (72.7*h) - 58
  print(f"O seu peso ideal é: {round(pesoIdeal, 1)}kg")
else:
  pesoIdeal = (62.1 * h) - 44.7
  print(f"O seu peso ideal é: {round(pesoIdeal, 1)}kg")