'''Faça um programa, com uma função que necessite de uma quantidade de argumentos indefinida, e um argumento de operação dos valores. Esta função deverá returnar o resultado da operação destes valores.'''

def soma(valores):
  resultado = 0 
  for x in valores:
    resultado += x
  return resultado

def calculadora(*valores, operacao='soma'):
  if (operacao=='soma'):
    return soma(valores)
  elif (operacao=='multiplicacao'):
    resultado = 1 
    for x in valores:
      resultado *= x
    return resultado
  elif (operacao=='divisao'):
    resultado = 1 
    for x in valores:
      resultado /= x
    return resultado  
  elif (operacao=='subtracao'):
    resultado = 0 
    for x in valores:
      resultado -= x
    return resultado

print(calculadora(1,1,1,4,72,6,operacao='soma'))