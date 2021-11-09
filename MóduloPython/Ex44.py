'''Crie um programa que receba um valor inteiro e avalie se ele é positivo ou negativo. Essa avaliação deve ocorrer dentro de uma função que retorna um valor booleano.'''

def verificaSinal():
  if n > 0:
    return print("Positivo")
  else:
    return print("Negativo")

n = int(input("Digite um número inteiro: "))
verificaSinal()