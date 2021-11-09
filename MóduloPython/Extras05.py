'''Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.'''

def inverte(numero):
  return str(numero)[::-1]

valor = int(input('Digite um numero: '))

print(inverte(valor))